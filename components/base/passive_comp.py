from components.base.static_comp import StaticComp

class PassiveComp(StaticComp):

  # TODO: Add notion of extendable, and composable props lists for passive!
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__var = self.package_var_args(*args)

  def package_var_args(self, *args):
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
    self.__var = self.package_var_args(*args, **kwargs)