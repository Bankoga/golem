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

  def __init__(self,item_id,pos,f_shape,s_shape=None):
    var = {
      'pos': pos,
      'f_shape': f_shape,
      's_shape': s_shape,
      'weights': ones(f_shape)
    }
    super().__init__(var, item_id=item_id,ctg=CtgType.DATA)
    


  # def set_up_weight(self, conv_shapes):
    # weights = {}
    # for shape in conv_shapes:
    #   weights[shape] = ones(shape.f_shape)
    # return weights
