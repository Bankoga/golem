from numpy import array, append

from components.func_sets.func_set import FuncSet
from utils.cardinators.cardinator_provider import cardinator_services
from data.axioms.configs import file_type
from data.enums.prop_types import SetType, PackType

from utils.config_reader import read
from utils.misc import heapsort
from utils.pos import Pos

class Proc(FuncSet):
  """
  A proc is used to create the stubs of some of the functional groups within a matrix
  PROC stands for primary repository of cells
  Groups of this type emulate or simulate (depending on degree of granularity) regions with only cells
  """
  def __init__(self, proc_id):
    self.config = read(proc_id,file_type['proc'])
    self._set_type_data_()
    super().__init__(self.config['id'], self.ctg_type)
    self._set_proc_groups_()
    self._set_outputs_()
    self._init_stage_data_()

  def _set_type_data_(self):
    self.name = self.config['type_data']['name']
    self.ctg_type = SetType[self.config['type_data']['type']]
    self.purpose = self.config['type_data']['purpose']
    self.cardinal_direction = self.config['type_data']['cardinal_direction']
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_proc_groups_(self):
    for i,group in enumerate(self.config['group_details']):
      self.groups[group['id']] = group
      # Are there processing group level types?
  
  def _set_group_prop_(self,conf_prop):
    for group in self.config[conf_prop]:
      self.groups[group][conf_prop] = self.config[conf_prop][group]
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_outputs_(self):
    conf_prop = 'outputs'
    self._set_group_prop_(conf_prop)
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _init_stage_data_(self):
    conf_obj = self.config['stages_to_groups_dict']
    sz = len(conf_obj)
    for i,stage in enumerate(conf_obj):
      for group in conf_obj[i]['groups']:
        ord_to_index = cardinator_services.get(self.cardinal_direction).get_card_index(i,sz)
        self.groups[group]['pos'] = Pos(z=ord_to_index)

  def process_inputs(self,inputs):
    """
    TODO: PERFORMANCE REFACTOR POINT
    This is run every timestep, and thus eats into the available processing resources quite extensively
    """
    results = {}
    for pack in inputs:
      p_type = pack.get_ctg()
      if p_type in results:
        results[p_type].append(pack)
      else:
        results[p_type] = [pack]
    if PackType.AGGREGATE in results:
      results[PackType.AGGREGATE] = heapsort(results[PackType.AGGREGATE])
      agg = None
      for pack in results[PackType.AGGREGATE]:
        if agg is None:
          agg = pack.var
        else:
          append(agg, pack.var)
      results[PackType.AGGREGATE] = agg
    return results