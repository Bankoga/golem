from components.func_sets.coders.coder import Coder
from components.axioms.configs import coder_ids
from components.enums.prop_types import FuncSetType

class PartsSensor(Coder):
  def __init__(self):
    super().__init__(coder_ids['ps'])

  def _set_type_data_(self):
    self.name = self.config['type_data']['name']
    self.ctg_type = FuncSetType[self.config['type_data']['type']]
    self.purpose = self.config['type_data']['purpose']
    self.rsp_freq = self.config['type_data']['rsp_freq']

class PartsSensorBuilder():
  def __init__(self):
    pass
  def __call__(self,**_ignored):
      return PartsSensor()