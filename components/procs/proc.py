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
    # self._set_hooks_from_()
    # self._set_hooks_to_()
    # self._set_links_defined_()
    # self._set_links_used_()

  def get_id(self):
    return self.id

  def _set_type_data_(self):
    self.name = self.config['type_data']['name']
    self.type = self.config['type_data']['type']
    self.purpose = self.config['type_data']['purpose']
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_proc_groups_(self):
    for i,group in enumerate(self.config['group_details']):
      self.groups[group['id']] = group
      # Are there processing group level types?
  
  def _set_group_prop_(self,conf_prop):
    for group in self.config[conf_prop]:
      self.groups[group][conf_prop] = self.config[conf_prop][group]

  def _set_group_hook_(self,hook_type):
    for group in self.config[hook_type]:
      self.groups[group][hook_type] = self.config[hook_type][group]

  # @abstractmethod # pylint: disable=undefined-variable
  def _set_inputs_(self):
    conf_prop = 'inputs'
    self._set_group_prop_(conf_prop)
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_outputs_(self):
    conf_prop = 'outputs'
    self._set_group_prop_(conf_prop)
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_hooks_from_(self):
    self._set_group_hook_('hooks_outof')
  
  # @abstractmethod # pylint: disable=undefined-variable
  def _set_hooks_to_(self):
    self._set_group_hook_('hooks_to')
  
  # @abstractmethod # pylint: disable=undefined-variable
  # def _set_links_defined_(self):
  #   pass
  
  # @abstractmethod # pylint: disable=undefined-variable
  # def _set_links_used_(self):
  #   pass
  
  # @abstractmethod # pylint: disable=undefined-variable
  # def _set_stage_groups_(self):
  #   pass