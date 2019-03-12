from components.base.passive_comp import PassiveComp

class ActiveComp(PassiveComp):

  def __init__(self, var, **kwargs):
    self.__base_set = False
    super().__init__(var, **kwargs)

  @property
  def base_set(self):
    return self.__base_set
  
  @base_set.setter
  def base_set(self,value):
    raise RuntimeError('The base var has already been set!')

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    self.__var = var
    if not self.base_set:
      self.base_var = self.var
      self.__base_set = True

  @property
  def base_var(self):
    return self.__base_var
  
  @base_var.setter
  def base_var(self, value):
    if self.base_set:
      raise RuntimeError('Setting the base var is not allowed!')
    else:
      self.__base_var = value

  def update(self, args, **kwargs):
    if len(args) == 1:
      self.var = args[0]
  
  def reset(self):
    if self.base_set:
      self.var = self.base_var
    else:
      raise RuntimeError('Attempted to reset an unset base')