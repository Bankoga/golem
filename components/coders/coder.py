from data.axioms.configs import file_type
from utils.config_reader import read
from components.ordinators.ordinator_provider import ordinator_services
from utils.pos import Pos

class Coder:
  """
  A sensor is used to create the stubs of the functional groups within a matrix
  """
  def __init__(self, coder_id):
    self.config = read(coder_id,file_type['coder'])
    self.id = self.config['id']
    self._set_type_data_()
    self.groups = dict()
    self._set_sensor_groups_()
    self._set_outputs_()
    self._set_hooks_()
    self._set_links_defined_()
    self._set_links_used_()
    self._init_stage_data_()

  def get_id(self):
    return self.id

  def _set_type_data_(self):
    self.name = self.config['type_data']['name']
    self.type = self.config['type_data']['type']
    self.purpose = self.config['type_data']['purpose']
    self.ordinal_direction = self.config['type_data']['ordinal_direction']
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_sensor_groups_(self):
    for i,group in enumerate(self.config['group_details']):
      self.groups[group['id']] = group
      # Are there sensoressing group level types?
  
  def _set_group_prop_(self,conf_prop):
    for group in self.config[conf_prop]:
      self.groups[group][conf_prop] = self.config[conf_prop][group]
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_outputs_(self):
    conf_prop = 'outputs'
    self._set_group_prop_(conf_prop)
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_hooks_(self):
    hook_prop = 'hooks'
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
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _init_stage_data_(self):
    conf_obj = self.config['stages_to_groups_dict']
    sz = len(conf_obj)
    for i,stage in enumerate(conf_obj):
      for group in conf_obj[i]['groups']:
        ord_to_index = ordinator_services.get(self.ordinal_direction).get_ord_index(i,sz)
        self.groups[group]['pos'] = Pos(z=ord_to_index)