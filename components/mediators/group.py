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

  @property
  def pct_of_stage(self):
    return self.var[2]
  @pct_of_stage.setter
  def pct_of_stage(self,value):
    self.setter_error()

  @property
  def nodes_details(self):
    return self.var[3]
  @nodes_details.setter
  def nodes_details(self,value):
    self.setter_error()
  
  def create_nodes(self, nodes_details):
    return []