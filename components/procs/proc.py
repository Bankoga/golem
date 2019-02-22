from components.func_groups.func_group import FuncGroup
from components.ordinators.ordinator_provider import ordinator_services
from data.axioms.configs import file_type

from utils.config_reader import read
from utils.pos import Pos

class Proc(FuncGroup):
  """
  A proc is used to create the stubs of some of the functional groups within a matrix
  PROC stands for primary repository of cells
  Groups of this type emulate or simulate (depending on degree of granularity) regions with only cells
  """
  def __init__(self, proc_id):
    self.config = read(proc_id,file_type['proc'])
    self.id = self.config['id']
    self._set_type_data_()
    self.groups = dict()
    self._set_proc_groups_()
    self._set_outputs_()
    self._init_stage_data_()

  def _set_type_data_(self):
    self.name = self.config['type_data']['name']
    self.type = self.config['type_data']['type']
    self.purpose = self.config['type_data']['purpose']
    self.ordinal_direction = self.config['type_data']['ordinal_direction']
  
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
        ord_to_index = ordinator_services.get(self.ordinal_direction).get_ord_index(i,sz)
        self.groups[group]['pos'] = Pos(z=ord_to_index)
