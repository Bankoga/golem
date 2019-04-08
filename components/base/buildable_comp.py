from abc import abstractmethod
from components.base.passive_comp import PassiveComp

class BuildableComp(PassiveComp):
  def __init__(self, *args, **kwargs):
    # args = []
    super().__init__(*args,**kwargs)

  def set_defaults(self):
    self.__is_built = False
    return super().set_defaults()

  @property
  def is_built(self):
    return self.__is_built

  @is_built.setter
  def is_built(self, value):
    raise RuntimeError('Cannot set the build status of a component. Simply build it!')

  def build(self, *args, **kwargs):
    if self.is_built:
      raise RuntimeError('Cannot build an already built component!')
    self.build_details(*args, **kwargs)
    self.__is_built = True
  
  @abstractmethod
  def build_details(self, *args, **kwargs):
    pass