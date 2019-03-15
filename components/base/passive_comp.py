from components.base.static_comp import StaticComp

class PassiveComp(StaticComp):

  def __init__(self, *args, **kwargs):
    super().__init__(kwargs['label'],kwargs['ctg'])
    # TODO: Rework var to be tuple based with getters and setters!
    self.__var = tuple(args)

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    raise RuntimeError('Vars cannot be set directly')