from components.base.plastic_comp import PlasticComp
from components.enums.pos import CtgType

class MatrixComp(PlasticComp):
  def __init__(self, var, **kwargs):
    kwargs['ctg']=CtgType.MATRIX
    super().__init__(var, **kwargs)