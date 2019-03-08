from numpy import ones

class ConvShape:

  """
  While ConvShapes are components, we need to break up the component base class into two types
  Why one asks? Because some components require building, and others don't
  Some require updates, but no builds, some require both, some are static
  """

  def __init__(self,f_shape,s_shape=None):
    self.f_shape = f_shape
    self.s_shape = s_shape
    self.weights = ones(f_shape)
    

  def conv(self, npmatrix):
    return 0

  # def set_up_weight(self, conv_shapes):
    # weights = {}
    # for shape in conv_shapes:
    #   weights[shape] = ones(shape.f_shape)
    # return weights
