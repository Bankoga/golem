from components.base.mechanisms.mechanism import Mechanism
from components.enums.pos import CtgType

class Stage(Mechanism):
  def __init__(self, *args, **kwargs):
    kwargs['ctg'] = CtgType.STAGE
    super().__init__(*args, **kwargs)