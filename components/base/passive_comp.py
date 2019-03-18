from components.base.static_comp import StaticComp

class PassiveComp(StaticComp):

  def __init__(self, *args, **kwargs):
    super().__init__(kwargs['label'],kwargs['ctg'])
    self.__var = self.prepare_args(*args)

  def prepare_args(self,*args):
    return tuple(args)

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    self.setter_error()
  
  def setter_error(self):
    raise RuntimeError('Cannot set var of passive component!')