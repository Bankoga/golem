from components.base.static_comp import StaticComp

class PassiveComp(StaticComp):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__var = self.prepare_var_args(*args, **kwargs)

  def prepare_var_args(self,*args, **kwargs):
    return tuple(args)

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    self.setter_error()
  
  def setter_error(self):
    raise RuntimeError('Cannot set var of component!')

  def update(self, *args, **kwargs):
    self.__var = self.prepare_var_args(*args, **kwargs)