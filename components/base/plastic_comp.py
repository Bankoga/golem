from components.base.passive_comp import PassiveComp

class PlasticComp(PassiveComp):

  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.__baseline = False

  @property
  def baseline(self):
    return self.__baseline
  
  @baseline.setter
  def baseline(self,value):
    if not self.baseline:
      self.__baseline = value
    else:
      raise RuntimeError('The base var has already been set!')

  def reset(self):
    if self.baseline:
      self.update(self.baseline)
    else:
      raise RuntimeError('Attempted to reset an unset base')