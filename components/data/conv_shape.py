from numpy import ones

from components.base.passive_comp import PassiveComp
from components.enums.pos import CtgType
from components.vars.data import ConvVar

class ConvShape(PassiveComp):

  """
  While ConvShapes are components, we need to break up the component base class into two types
  Why one asks? Because some components require building, and others don't
  Some require updates, but no builds, some require both, some are static
  the position is relative to its parents X,Y (or row/column) index within stage Z
  """

  def __init__(self,f_shape,s_shape=None, **kwargs):
    kwargs['ctg']=CtgType.DATA
    super().__init__(f_shape,s_shape,ones(f_shape), **kwargs)

  def prepare_args(self, *args):
    return ConvVar(*args)

  @property
  def weights(self):
    return self.var.weights
  
  @weights.setter
  def weights(self, value):
    self.setter_error()

  @property
  def filter_shape(self):
    return self.var.filter_shape
  
  @filter_shape.setter
  def filter_shape(self, value):
    self.setter_error()

  @property
  def spacing_shape(self):
    return self.var.spacing_shape
  
  @spacing_shape.setter
  def spacing_shape(self, value):
    self.setter_error()