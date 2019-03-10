from abc import abstractmethod
from components.base.component import Component
from data.enums.prop_types import RuleType

class Instruction(Component):
  def __init__(self, itm_id, rtype, pos):
    self.item_label = f'{rtype.name}-{pos.get_hash()}'
    # hash(self.item_label)
    # What is the id of AN instruction in the matrix?
    # some func of type name, shape, position, and ?
    super().__init__(itm_id, rtype.get_component_type(), rtype)
    self.curr_shape = None
    self.curr_bearing = None
    self.curr_pos = None
    self.pos = pos
    
  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  @abstractmethod
  def perform(self,inputs):
    pass
  
  @abstractmethod
  def set_up_weights(self, shapes):
    pass
  
  def build(self,data=None):
    super().build(data)
  
  def reset(self):
    pass

  def update(self, new_data):
    super().update(new_data)