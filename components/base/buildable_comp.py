from abc import abstractmethod
from components.base.passive_comp import PassiveComp

class BuildableComp(PassiveComp):
  def __init__(self, *args, **kwargs):
    args = []
    super().__init__(*args,**kwargs)
    self.__is_built = False

  @property
  def is_built(self):
    return self.__is_built

  @is_built.setter
  def is_built(self, value):
    raise RuntimeError('Cannot set the build status of a component. Simply build it!')

  @abstractmethod
  def build(self, *args, **kwargs):
    if self.is_built:
      raise RuntimeError('Cannot build an already built component!')
    self.build_details(*args, **kwargs)
  
  def build_details(self, *args, **kwargs):
    self.update(*args)
    self.__is_built = True