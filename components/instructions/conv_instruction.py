from data.enums.prop_types import RuleType

from components.instructions.instruction import Instruction

class ConvInstruction(Instruction):
  def __init__(self,itm_id,direction,conv_shapes,source_ind,source_shape,pos):
    super().__init__(itm_id,RuleType.CONV, pos)
    self.shape = source_shape
    self.direction = direction
    self.ind = source_ind
    self.build(conv_shapes)
  
  def conv(self, npmatrix):
    return 0

  def build(self, data=None):
    # weights = self.set_up_weights(self.conv_shapes)
    if (self._built_):
      raise RuntimeError('This is not yet implemented')
    else:
      super().build(data)
  
  def reset(self):
    raise RuntimeError('This is not yet implemented')

  def update(self, new_data):
    raise RuntimeError('This is not yet implemented')

  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  def operate(self,inputs=None,context=None):
    super().operate()
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

  def update_weight(self):
    pass