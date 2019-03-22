from components.base.workers.consumer_comp import ConsumerComp
from components.enums.prop_types import RuleType
from components.enums.pos import CtgType

class Instruction(ConsumerComp):
  """
  Instruction: An algorithm for turning a buffer of inputs into outputs for a channel
  """
  # for nested cardinal rotations, apply each rotation by its value/the number of rotations
  def __init__(self, *args, **kwargs):
    if not 'label' in kwargs and not kwargs['label'] is None:
      kwargs['label'] = f'{args[0].name}-{hash(args[1])}'
    kwargs['ctg'] = CtgType.INSTRUCTION
    super().__init__(*args, **kwargs)

  def prepare_args(self,*args):
    self.__prev_data = []
    return super().prepare_args(*args)

  @property
  def prev_data(self):
    return self.__prev_data
  
  @prev_data.setter
  def prev_data(self, value):
    raise RuntimeError('Prev Data cannot be set!')

  def operate(self,curr_data=[]):
    try:
      super().operate()
      self.__prev_data = curr_data
      return True
    except:
      return False