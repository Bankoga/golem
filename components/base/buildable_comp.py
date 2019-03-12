from components.base.passive_comp import PassiveComp

class BuildableComp(PassiveComp):
  def __init__(self, **kwargs):
    self.__is_built = False
    super().__init__(None,**kwargs)

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    if self.is_built:
      raise RuntimeError('Cannot set the var of a built component!')
    else:
      self.__var = var

  @property
  def is_built(self):
    return self.__is_built

  @is_built.setter
  def is_built(self, value):
    raise RuntimeError('Cannot set the build status of a component. Simply build it!')

  def build(self, value):
    if self.is_built:
      raise RuntimeError('Cannot build an already built component!')
    self.var = value
    self.__is_built = True