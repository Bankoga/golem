from components.base.static_comp import StaticComp

class PassiveComp(StaticComp):

  def __init__(self, var, **kwargs):
    super().__init__(kwargs['label'],kwargs['ctg'])
    # TODO: Rework var to be tuple based with getters and setters!
    self.var = var

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    self.__var = var