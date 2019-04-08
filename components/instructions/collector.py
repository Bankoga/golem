from components.enums.prop_types import RuleType
from components.data.collector_segment import CollectorSegment
from components.instructions.instruction import Instruction
from utils.helpers.prop_gen_help import roll_name
from numpy import array, zeros
from utils.pos import diff_addrs

class Collector(Instruction):
  """
  Collectors are for grabbing parent specific resource availability data from a defined set of addresses
  args: registry,source_index,source_shape,step_direction,num_steps,resource_accepted,segment_defs
  """
  def __init__(self,*args,**kwargs):
    super().__init__(*args, **kwargs)

  @property
  def attenuation_rate(self):
    return 2.5
  @attenuation_rate.setter
  def attenuation_rate(self,value):
    raise RuntimeError('Can not set the value of attenuation_rate!')

  @property
  def source_index(self):
    return self.var[1]
  @source_index.setter
  def source_index(self,value):
    raise RuntimeError('Can not set the value of source_index!')

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
  def segment_defs(self):
    return self.var[6]
  @segment_defs.setter
  def segment_defs(self,value):
    raise RuntimeError('Can not set the value of segment_defs!')

  @property
  def leaves(self):
    return self.__leaves
  @leaves.setter
  def leaves(self,value):
    raise RuntimeError('Can not set the value of leaves!')

  def build_details(self, *args, **kwargs):
    super().build_details(*args, **kwargs)
    self.set_up_collector_segments(self.segment_defs)

  def set_up_collector_segments(self, shape_defs):
    res = []
    for item in shape_defs:
      res.append(CollectorSegment(residence_address=item[0],source_address=self.address,source_index=self.source_index,fill_shape=item[1],label=f'{self.label}_{roll_name()}'))
    self.__leaves = res

  def conv(self, npmatrix):
    return 0

  def instruction_details(self,curr_data=[],inputs=None,context=None):
    res = []
    for i, cllct_sgmnt in enumerate(self.leaves):
      if len(curr_data) > i:
        res.append(cllct_sgmnt.apply(curr_data[i]))
      else:
        res.append(zeros(cllct_sgmnt.weights.shape))
    return res