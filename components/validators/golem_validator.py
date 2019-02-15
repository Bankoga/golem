from validators.validator import Validator

class GolemValidator(Validator):
  def __init__(self):
    super.__init__('')
    pass

class GolemValidatorBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = GolemValidator()
    return self._instance
