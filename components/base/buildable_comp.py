from components.base.passive_comp import PassiveComp

class BuildableComp(PassiveComp):
  def __init__(self, *args, **kwargs):
    super().__init__(None,**kwargs)
    self.__is_built = False

  @property
  def is_built(self):
    return self.__is_built

  @is_built.setter
  def is_built(self, value):
    raise RuntimeError('Cannot set the build status of a component. Simply build it!')

  def build(self, *args):
    if self.is_built:
      raise RuntimeError('Cannot build an already built component!')
    self.update(*args)
    self.__is_built = True
