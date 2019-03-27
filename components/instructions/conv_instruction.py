from components.enums.prop_types import RuleType
from components.data.collector_segment import CollectorSegment
from components.instructions.instruction import Instruction
from utils.helpers.prop_gen_help import roll_name

class ConvInstruction(Instruction):
  def __init__(self,registry,source_ind,source_shape,step_direction,num_steps,resource_accepted,collector_segment_defs,**kwargs):
    args = [registry, source_ind, source_shape, step_direction, num_steps, resource_accepted, collector_segment_defs]
    super().__init__(*args, **kwargs)
    # self.set_up_collector_segments(self.collector_segment_defs)
    # self.shape = source_shape
    # self.step_direction = step_direction
    # self.ind = source_ind
    # each conv shape represents a step to take in a direction during the sampling process
  
  def set_up_collector_segments(self, shape_defs):
    res = []
    for shapes in shape_defs:
      res.append(CollectorSegment(*shapes,label=f'{self.label}_{roll_name()}'))
    self.__collector_segments = res
  def conv(self, npmatrix):
    return 0


  @property
  def source_ind(self):
    return self.var[1]

  @source_ind.setter
  def source_ind(self,value):
    raise RuntimeError('Can not set the value of source_ind!')

  @property
  def source_shape(self):
    return self.var[2]

  @source_shape.setter
  def source_shape(self,value):
    raise RuntimeError('Can not set the value of source_shape!')

  @property
  def step_direction(self):
    return self.var[3]

  @step_direction.setter
  def step_direction(self,value):
    raise RuntimeError('Can not set the value of step_direction!')

  @property
  def num_steps(self):
    return self.var[4]

  @num_steps.setter
  def num_steps(self,value):
    raise RuntimeError('Can not set the value of num_steps!')

  @property
  def resource_accepted(self):
    return self.var[5]

  @resource_accepted.setter
  def resource_accepted(self,value):
    raise RuntimeError('Can not set the value of resource_accepted!')
  
  @property
  def collector_segment_defs(self):
    return self.var[6]

  @collector_segment_defs.setter
  def collector_segment_defs(self,value):
    raise RuntimeError('Can not set the value of collector_segment_defs!')

  @property
  def collector_segments(self):
    return self.__collector_segments

  @collector_segments.setter
  def collector_segments(self,value):
    raise RuntimeError('Can not set the value of collector_segments!')

  def build_details(self, *args, **kwargs):
    super().build_details(*args, **kwargs)
    self.set_up_collector_segments(self.collector_segment_defs)



  def get_side_szs(self, side_sz):
    x_sz = side_sz
    y_sz = side_sz
    if type(side_sz) is tuple:
      x_sz = side_sz[0]
      y_sz = side_sz[1]
    return (x_sz,y_sz)

  def extract_quadrant(self, input_ind, input_shape,side_sz):
    x = input_ind[0]
    x_sz, y_sz = self.get_side_szs(side_sz)
    if len(input_ind) > 1:
      y = input_ind[1]
      quadrant = input_shape[x:x+x_sz][y:y+y_sz]
    else:
      quadrant = input_shape[x:x+x_sz]
    return quadrant

  def apply_collector_segment(self, cnv_shp, resource_data):
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