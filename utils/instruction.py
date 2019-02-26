from abc import abstractmethod

class Instruction:
  def __init__(self, rtype, pos):
    self.type = rtype
    self.curr_shape = None
    self.curr_bearing = None
    self.curr_pos = None
    self.pos = pos

  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  @abstractmethod
  def perform(self,package):
    pass