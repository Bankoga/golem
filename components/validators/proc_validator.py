from validators.validator import Validator

class ProcValidator(Validator):
  def __init__(self, proc_id):
    super.__init__(proc_id)
    pass

class ProcValidatorBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,proc_id,**_ignored):
    if not self._instance:
      self._instance = ProcValidator(proc_id)
    return self._instance
