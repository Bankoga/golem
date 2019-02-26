from data.axioms.enums import RuleType

from utils.instruction import Instruction

class ConvInstruction(Instruction):
  def __init__(self,directions,shapes):
    super().__init__(RuleType.CELL)
    self.directions = directions
    self.shapes = shapes
    
  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  def perform(self,package):
    pass