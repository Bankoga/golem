from components.enums.prop_types import RuleType

from components.instructions.instruction import Instruction

class ConvInstruction(Instruction):
  def __init__(self,registry,direction,resource,conv_shapes,source_ind,source_shape,**kwargs):
    args = [registry, direction, resource, conv_shapes, source_ind, source_shape]
    super().__init__(*args, **kwargs)
    # self.shape = source_shape
    # self.direction = direction
    # self.ind = source_ind
    # each conv shape represents a step to take in a direction during the sampling process
    
  def conv(self, npmatrix):
    return 0

  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  def instruction_details(self,curr_data=[],inputs=None,context=None):
    res = 0
    # for each read, we change the Z in the direction supplied using the PROPER cardinator
    #  we also change the size of the sample
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

  def extract_quadrant(self, side_sz, input_ind, input_shape):
    return []


  def update_weight(self):
    pass