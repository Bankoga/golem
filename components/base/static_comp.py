from utils.validators.pos_validators import is_valid_ctg
from utils.validators.prop_validators import is_valid_id

class StaticComp:
  def __init__(self, label, ctg):
    self.label = label
    self.ctg = ctg

  @property
  def label(self):
    return self.__label

  @property
  def ctg(self):
    return self.__ctg

  @label.setter
  def label(self, value): # pylint: disable=function-redefined
    if not is_valid_id(value):
      raise ValueError('INVALID ID!')
    else:
      self.__label = value

  @ctg.setter
  def ctg(self, value): # pylint: disable=function-redefined
    if not is_valid_ctg(value):
      raise ValueError('INVALID CATEGORY!')
    else:
      self.__ctg = value