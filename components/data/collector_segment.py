from numpy import array, ones

from components.base.segment import Segment
from components.base.plastic_comp import PlasticComp
from components.enums.pos import CtgType
from utils.helpers.arrayer import get_sizes, get_quantity

class CollectorSegment(PlasticComp, Segment):

  def __init__(self,*args, **kwargs):
    has_label = ('label' in kwargs and not kwargs['label'] is None)
    if not has_label:
      kwargs['label'] = ''
    kwargs['ctg']=CtgType.DATA
    super().__init__(*args, **kwargs)
    self.__fill_shape = kwargs['fill_shape']
    self.shape = kwargs['fill_shape']
    self.collection_chances = ones(kwargs['fill_shape'])

  def set_weighted_defaults(self):
    shape = tuple([1])
    super().set_weighted_defaults(shape=shape,weights=ones(shape))
    self.__collection_chances = ones(shape)

  @property
  def fill_shape(self):
    return self.__fill_shape
  @fill_shape.setter
  def fill_shape(self, value):
    self.__fill_shape = value
    self.shape = value
    self.__collection_chances = ones(value)
  
  @property
  def collection_chances(self):
    return self.__collection_chances
  @collection_chances.setter
  def collection_chances(self, value):
    self.__collection_chances = value

  def apply(self, resource_data):
    """
    This returns the resources actually available for useage by the parent of the collector
    Everything is assumed to be presented in 2d slices.
    """
    if len(resource_data.shape) != 2:
      raise RuntimeError('Collector segments expect the world to be presented in 2D slices')
    actuals = []
    for i,row in enumerate(self.weights):
      row_actuals = []
      for j,weight in enumerate(row):
        actual = round(min(weight, get_quantity(resource_data,i,j)), 5)
        row_actuals.append(actual)
      actuals.append(row_actuals)
    return array(actuals)