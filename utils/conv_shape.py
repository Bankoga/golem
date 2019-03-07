from numpy import ones

class ConvShape:

  def __init__(self,f_shape,s_shape=None):
    self.f_shape = f_shape
    self.s_shape = s_shape
    self.weights = ones(f_shape)
    
  # def set_up_weight(self, conv_shapes):
    # weights = {}
    # for shape in conv_shapes:
    #   weights[shape] = ones(shape.f_shape)
    # return weights
