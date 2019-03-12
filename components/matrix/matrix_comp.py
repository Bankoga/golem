from components.base.active_comp import ActiveComp
from components.enums.pos import CtgType

class MatrixComp(ActiveComp):
  def __init__(self, var, **kwargs):
    kwargs['ctg']=CtgType.MATRIX
    super().__init__(var, **kwargs)