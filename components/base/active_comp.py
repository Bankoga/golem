from components.base.static_comp import StaticComp

class ActiveComp(StaticComp):

  def __init__(self, *args, **kwargs):
    super().__init__(kwargs['label'],kwargs['ctg'])
    self.__baseline = False
    self.__var = tuple(args)

  @property
  def baseline(self):
    return self.__baseline
  
  @baseline.setter
  def baseline(self,value):
    if not self.baseline:
      self.__baseline = value
    else:
      raise RuntimeError('The base var has already been set!')

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    self.setter_error()
  
  def update(self, *args):
    self.__var = tuple(args)
  
  def reset(self):
    if self.baseline:
      self.__var = self.baseline
    else:
      raise RuntimeError('Attempted to reset an unset base')
  
  def setter_error(self):
    raise RuntimeError('Cannot set var of active component directly! Must use update!')