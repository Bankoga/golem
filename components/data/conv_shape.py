from numpy import ones

from components.base.passive_comp import PassiveComp

from components.enums.pos import CtgType

class ConvShape(PassiveComp):

  """
  While ConvShapes are components, we need to break up the component base class into two types
  Why one asks? Because some components require building, and others don't
  Some require updates, but no builds, some require both, some are static
  the position is relative to its parents X,Y (or row/column) index within stage Z
  """

  def __init__(self,label,pos,f_shape,s_shape=None):
    self.pos = pos
    self.f_shape = f_shape
    self.s_shape = s_shape
    var = ones(f_shape)
    super().__init__(var, label=label,ctg=CtgType.DATA)

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, new_weights):
    self.__var = new_weights

  # def set_up_weight(self, conv_shapes):
    # weights = {}
    # for shape in conv_shapes:
    #   weights[shape] = ones(shape.f_shape)
    # return weights
