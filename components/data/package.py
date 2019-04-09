from components.base.passive_comp import PassiveComp
from components.enums.pos import CtgType

class Package(PassiveComp):
  def __init__(self, *args, **kwargs):
    kwargs['ctg'] =  CtgType.DATA
    super().__init__(*args,**kwargs)
  
  @property
  def data(self):
    return self.var[0]
  @data.setter
  def data(self, value):
    raise RuntimeError('Can not set value of data')

  @property
  def recipient(self):
    return self.var[1]
  @recipient.setter
  def recipient(self, value):
    raise RuntimeError('Can not set value of recipient')
  
  @property
  def sender(self):
    return self.var[2]
  @sender.setter
  def sender(self, value):
    raise RuntimeError('Can not set value of sender')