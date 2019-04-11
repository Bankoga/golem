from components.base.mechanisms.mechanism import Mechanism
from components.enums.pos import CtgType

class Group(Mechanism):
  def __init__(self, *args, **kwargs):
    kwargs['ctg'] = CtgType.GROUP
    super().__init__(*args,**kwargs)

  @property
  def group_type(self):
    return self.var[1]
  
  @group_type.setter
  def group_type(self,value):
    self.setter_error()