from data.axioms.enums import RuleType

from components.instructions.instruction import Instruction

from numpy import ones,diag

class ConvInstruction(Instruction):
  def __init__(self,direction,shapes,pos):
    super().__init__(RuleType.CELL, pos)
    self.direction = direction
    self.shapes = shapes
    self.set_up_weights(shapes)
    
  def set_up_weights(self, shapes):
    weights = {}
    for shape in shapes:
      weights[shape] = ones(shape)
    return weights

  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  def perform(self,inputs):
    res = 0
    # for each read, we change the Z in the direction supplied using the PROPER cardinator
    #   this means we either have to be given the cardinator
    #   OR
    #   we have to be able to select the cardinator
    #   so that we can get_card_index(ind, inputs)
    #   context.get_inputs_at_steps_in(direction, inputs)
    #   input_pack = select the inputs using our Pos info plus the card index
    #   patch = extract a slice from the input_pack according to the current shape
    #   step_res = shape.weights * patch
    #   res.append(step_res * abs(diff(ind,self.pos.z)))
    # we only return the step_res from a perform, so as to handle plasticity at the function group level
    return res

  def update_weight(self):
    pass