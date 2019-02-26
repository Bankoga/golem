from data.axioms.enums import RuleType

from components.instructions.instruction import Instruction

from numpy import identity

class ConvInstruction(Instruction):
  def __init__(self,direction,shapes, pos):
    super().__init__(RuleType.CELL, pos)
    self.direction = direction
    self.shapes = shapes
    self.set_up_weights(shapes)
    
  def set_up_weights(self, shapes):
    weights = {}
    for shape in shapes:
      weights[shape] = identity(shape)
    return weights

  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  def perform(self,package):
    pass

  def update_weight(self):
    pass