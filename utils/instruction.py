from abc import abstractmethod

class Instruction:
  def __init__(self, rtype):
    self.type = rtype
    self.curr_shape = None
    self.curr_bearing = None
    self.curr_pos = None

  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  @abstractmethod
  def perform(self,package):
    pass