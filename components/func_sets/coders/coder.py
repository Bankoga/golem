from data.axioms.configs import file_type
from utils.config_reader import read
from utils.cardinators.cardinator_provider import cardinator_services
from utils.pos import Pos
from components.func_sets.func_set import FuncSet
from data.enums.prop_types import SetType


class Coder(FuncSet):
  """
  A sensor is used to create the stubs of the functional groups within a matrix
  """
  def __init__(self, coder_id):
    self.config = read(coder_id,file_type['coder'])
    self._set_type_data_()
    super().__init__(self.config['id'], self.ctg_type)
    self.groups = dict()
    self._set_sensor_groups_()
    self._set_outputs_()
    self._set_hooks_()
    self._set_links_defined_()
    self._set_links_used_()

  def _set_type_data_(self):
    self.name = self.config['type_data']['name']
    self.ctg_type = SetType[self.config['type_data']['type']]
    self.purpose = self.config['type_data']['purpose']
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_sensor_groups_(self):
    for i,group in enumerate(self.config['groups']):
      self.groups[group['id']] = group
      self.groups[group['id']]['pos'] = Pos(z=0)
      # Are there sensoressing group level types?
  
  def _set_group_prop_(self,conf_prop):
    if not self.config[conf_prop]:
      for group in self.groups:
        self.groups[group][conf_prop] = dict()
    else:
      for group in self.config[conf_prop]:
        self.groups[group][conf_prop] = self.config[conf_prop][group]
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_outputs_(self):
    conf_prop = 'outputs'
    self._set_group_prop_(conf_prop)
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_hooks_(self):
    hook_prop = 'hooks'
    if not self.config[hook_prop]:
      for group in self.groups:
        self.groups[group][hook_prop] = []
    else:
      for hook_type in self.config[hook_prop]:
        for group in self.groups:
          if hook_prop not in self.groups[group]:
            self.groups[group][hook_prop] = [hook_type]
          else:
            self.groups[group][hook_prop].append(hook_type)

  # @abstractmethod # pylint: disable=undefined-variable
  def _build_links_(self, link_protos, link_results):
    if link_protos is not None:
      for link in link_protos:
        link_results[link['id']] = link
    return link_results

  # @abstractmethod # pylint: disable=undefined-variable
  def _set_links_defined_(self):
    links_defined = self.config['links_defined']
    link_defs = dict()
    self.link_definitions = self._build_links_(links_defined,link_defs)
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_links_used_(self):
    links_used = self.config['links_used']
    prcd_lu = {}
    self.links_used = self._build_links_(links_used, prcd_lu)