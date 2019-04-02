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
  
  def get_side_szs(self, side_szs):
    x_sz = side_szs
    y_sz = side_szs
    if type(side_szs) is tuple:
      x_sz = side_szs[0]
      y_sz = side_szs[1]
    return (x_sz,y_sz)

  def extract_quadrant(self, input_ind, input_shape,side_szs):
    x = input_ind[0]
    x_sz, y_sz = self.get_side_szs(side_szs)
    if len(input_ind) > 1:
      y = input_ind[1]
      quadrant = input_shape[x:x+x_sz][y:y+y_sz]
    else:
      quadrant = input_shape[x:x+x_sz]
    return quadrant

  def get_quantity(self, resource_data, i, j=None):
    if len(resource_data) > 1:
      try:
        quantity = resource_data[i][j]
      except:
        quantity = 0
    else:
      try:
        quantity = resource_data[i]
      except:
        quantity = 0
    return quantity

  def apply(self, resource_data):
    """
    This returns the resources actually available for useage by the parent of the collector
    """

    # TODO: rework entirely bc is broken
    actuals = []
    return array(actuals)
