from numpy import array, ones

from components.base.segment import Segment
from components.base.plastic_comp import PlasticComp
from components.enums.pos import CtgType

class CollectorSegment(PlasticComp, Segment):

  def __init__(self,*args, **kwargs):
    has_label = ('label' in kwargs and not kwargs['label'] is None)
    if not has_label:
      kwargs['label'] = ''
    kwargs['ctg']=CtgType.DATA
    super().__init__(**kwargs)

  def prepare_var_args(self, *args, **kwargs):
    if kwargs['fill_shape']:
      self.shape = kwargs['fill_shape']
    else:
      self.shape = ()
    return super().prepare_var_args(*args, **kwargs)

  def set_weighted_defaults(self):
    shape = tuple([1])
    super().set_weighted_defaults(shape=shape,weights=ones(shape))

  def update(self, *args):
    super().update(*args)