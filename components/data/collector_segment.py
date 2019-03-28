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

  def __init__(self,f_shape, **kwargs):
    has_label = ('label' in kwargs and not kwargs['label'] is None)
    if not has_label:
      kwargs['label'] = ''
    kwargs['ctg']=CtgType.DATA
    super().__init__(f_shape, **kwargs)

  def set_weighted_defaults(self):
    shape = tuple([1])
    super().set_weighted_defaults(shape=shape,weights=ones(shape))

  @property
  def fill_shape(self):
    return self.var[0]
  
  @fill_shape.setter
  def fill_shape(self, value):
    self.setter_error()
  
  def update(self, *args):
    super().update(*args)
    self.shape = self.fill_shape