from data.axioms.configs import file_type
from utils.config_reader import read

class Proc:
  """
  A proc is used to create the stubs of the functional groups within a matrix
  """
  def __init__(self, proc_id):
    self.config = read(proc_id,file_type['proc'])
    self.id = self.config['id']
    self._set_type_data_()
    self.groups = dict()
    self._set_proc_groups_()
    self._set_inputs_()
    self._set_outputs_()
    self._set_hooks_()
    self._set_links_defined_()
    self._set_links_used_()

  def get_id(self):
    return self.id

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
  def _set_inputs_(self):
    conf_prop = 'inputs'
    self._set_group_prop_(conf_prop)
  
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
  def _build_links_(self, link_protos, link_results=dict()):
    if link_protos is not None:
      for link in link_protos:
        link_results[link['id']] = link
    return link_results

  # @abstractmethod # pylint: disable=undefined-variable
  def _set_links_defined_(self):
    links_defined = self.config['links_defined']
    link_defs = dict()
    if links_defined is not None:
      for link in links_defined:
        link_defs[link['id']] = link
    self.link_definitions = link_defs
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_links_used_(self):
    links_used = self.config['links_used']
    self.links_used = self._build_links_(links_used)
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _init_stage_data_(self):
    pass