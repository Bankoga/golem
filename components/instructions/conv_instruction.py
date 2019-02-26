from data.axioms.enums import RuleType

from components.instructions.instruction import Instruction

class ConvInstruction(Instruction):
  def __init__(self,directions,shapes, pos):
    super().__init__(RuleType.CELL, pos)
    self.directions = directions
    self.shapes = shapes
    
  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  def perform(self,package):
    pass