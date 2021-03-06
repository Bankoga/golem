from utils.validators.pos_validators import is_valid_ctg
from utils.validators.prop_validators import is_valid_label

class StaticComp:
  def __init__(self, *args, **kwargs):
    """
    every entity is larger and smaller than itself
    though itself yet it remains
    forever embedded within context
    a place is a thing and a thing is place
    """
    # TODO: Unify label and lineage! Different representations of the same thing
    self.label = kwargs['label']
    self.ctg = kwargs['ctg']
    self.set_defaults()

  def set_defaults(self):
    return True

  @property
  def label(self):
    return self.__label

  @property
  def ctg(self):
    return self.__ctg

  @label.setter
  def label(self, value): # pylint: disable=function-redefined
    if not is_valid_label(value):
      raise ValueError('INVALID ID!')
    else:
      self.__label = value

  @ctg.setter
  def ctg(self, value): # pylint: disable=function-redefined
    if not is_valid_ctg(value):
      raise ValueError('INVALID CATEGORY!')
    else:
      self.__ctg = value