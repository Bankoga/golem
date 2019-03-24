from numpy import array, ones

from components.base.plastic_comp import PlasticComp
from components.enums.pos import CtgType
from components.vars.data import ConvVar

class ConvShape(PlasticComp):

  """
  While ConvShapes are components, we need to break up the component base class into two types
  Why one asks? Because some components require building, and others don't
  Some require updates, but no builds, some require both, some are static
  the position is relative to its parents X,Y (or row/column) index within stage Z
  """

  def __init__(self,f_shape,s_shape=None, **kwargs):
    has_label = ('label' in kwargs and not kwargs['label'] is None)
    if not has_label:
      kwargs['label'] = ''
    kwargs['ctg']=CtgType.DATA
    super().__init__(f_shape,s_shape, **kwargs)

  def set_weighted_defaults(self):
    shape = tuple([1])
    super().set_weighted_defaults(shape=shape,weights=ones(shape))

  def prepare_var_args(self, *args):
    res = ConvVar(*args)
    self.shape = res.filter_shape
    return res

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
  
  def update(self, *args):
    super().update(*args)
    self.shape = self.filter_shape