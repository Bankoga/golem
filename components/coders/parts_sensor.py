from components.coders.coder import Coder
from data.axioms.configs import coder_ids

class PartsSensor(Coder):
  def __init__(self):
    super().__init__(coder_ids['ps'])
    
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

class PartsSensorBuilder():
  def __init__(self):
    pass
  def __call__(self,**_ignored):
      return PartsSensor()