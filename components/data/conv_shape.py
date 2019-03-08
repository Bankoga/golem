from numpy import ones

class ConvShape:

  """
  While ConvShapes are components, we need to break up the component base class into two types
  Why one asks? Because some components require building, and others don't
  Some require updates, but no builds, some require both, some are static
  the position is relative to its parents X,Y (or row/column) index within stage Z
  """

  def __init__(self,pos,f_shape,s_shape=None):
    self.pos = pos
    self.f_shape = f_shape
    self.s_shape = s_shape
    self.weights = ones(f_shape)
    


  # def set_up_weight(self, conv_shapes):
    # weights = {}
    # for shape in conv_shapes:
    #   weights[shape] = ones(shape.f_shape)
    # return weights
