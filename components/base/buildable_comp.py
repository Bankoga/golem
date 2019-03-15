from components.base.static_comp import StaticComp

class BuildableComp(StaticComp):
  def __init__(self, **kwargs):
    super().__init__(kwargs['label'],kwargs['ctg'])
    self.__is_built = False

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, *args):
    if self.is_built:
      raise RuntimeError('Cannot set the var of a built component!')
    else:
      self.__var = tuple(*args)

  @property
  def is_built(self):
    return self.__is_built

  @is_built.setter
  def is_built(self, value):
    raise RuntimeError('Cannot set the build status of a component. Simply build it!')

  def build(self, *args):
    if self.is_built:
      raise RuntimeError('Cannot build an already built component!')
    self.var = args
    self.__is_built = True