from components.base.mechanisms.mechanism import Mechanism
from components.enums.pos import CtgType
from components.mediators.group import Group
from utils.helpers.arrayer import get_sizes

class Stage(Mechanism):
  def __init__(self, *args, **kwargs):
    kwargs['ctg'] = CtgType.STAGE
    super().__init__(*args, **kwargs)
  
  @property
  def shape(self):
    return self.var[1]
  @shape.setter
  def shape(self, value):
    self.setter_error()
  
  @property
  def group_defs(self):
    return self.var[2]
  @group_defs.setter
  def group_defs(self, value):
    self.setter_error()
  
  def create_layer(self, group_def):
    layer = []
    x,y = get_sizes(self.shape)
    for row in range(x):
      for col in range(y):
        index = (row,col)
        group = Group(self.registry,
                      group_def['group_type'],
                      index,
                      self.shape,
                      group_def['pct_of_stage'],
                      group_def['node_details'],
                      label=f'{group_def["label"]}_{row}_{col}')
        layer.append(group)
    return layer

  def create_groups(self, group_defs):
    groups = []
    for group_def in group_defs:
      layer = self.create_layer(group_def)
      groups.extend(layer)
    return groups