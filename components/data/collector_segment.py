from numpy import array, ones

from components.base.plastic_comp import PlasticComp
from components.enums.pos import CtgType

class CollectorSegment(PlasticComp):

  """
  While CollectorSegments are components, we need to break up the component base class into two types
  Why one asks? Because some components require building, and others don't
  Some require updates, but no builds, some require both, some are static
  the position is relative to its parents X,Y (or row/column) index within stage Z
  """

  def __init__(self,address,source_index,f_shape, **kwargs):
    has_label = ('label' in kwargs and not kwargs['label'] is None)
    if not has_label:
      kwargs['label'] = ''
    kwargs['ctg']=CtgType.DATA
    super().__init__(address,source_index,f_shape, **kwargs)

  def prepare_var_args(self, *args, **kwargs):
    if len(args) > 2:
      self.shape = args[2]
    else:
      self.shape = ()
    return super().prepare_var_args(*args, **kwargs)

  def set_weighted_defaults(self):
    shape = tuple([1])
    super().set_weighted_defaults(shape=shape,weights=ones(shape))

  @property
  def address(self):
    return self.var[0]
  @address.setter
  def address(self, value):
    self.setter_error()
    
  @property
  def source_index(self):
    return self.var[1]
  @source_index.setter
  def source_index(self, value):
    self.setter_error()

  @property
  def fill_shape(self):
    return self.var[2]
  @fill_shape.setter
  def fill_shape(self, value):
    self.setter_error()
  
  def update(self, *args):
    super().update(*args)
    self.shape = self.fill_shape