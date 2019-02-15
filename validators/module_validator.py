from validators.validator import Validator

class ModuleValidator(Validator):
  def __init__(self):
    super.__init__('')
    pass

  def input_melds_validation(self):
    return False
  def proc_type_validation(self,proc_type):
    return False
  def proc_stage_groups_dict_validation(self):
    return False
  def proc_stage_shape_validation(self):
    return False
  def proc_group_input_melds_validation(self):
    return False
  def proc_group_details_validation(self):
    return False
  def proc_group_output_melds_validation(self):
    return False
  def proc_output_melds_validation(self):
    return False
  def shape_composition_validation(self):
    return False
  def output_melds_validation(self):
    return False
  def link_melds_validation(self):
    return False
  def links_defined_validation(self):
    return False

class ModuleValidatorBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = ModuleValidator()
    return self._instance
