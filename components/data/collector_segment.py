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

  def apply(self, resource_data):
    """
    This returns the resources actually available for useage by the parent of the collector
    """
    # diff_mag = diff_addrs(coll_sgmnt.address, self.address)
    # adjusted_weights = (coll_sgmnt.weights - (diff_mag*self.attenuation_rate))
    x = resource_data[0]
    x_sz, y_sz = self.get_side_szs(self.fill_shape)
    actuals = []
    if len(resource_data) > 1:
      y = resource_data[1]
      for i,row in enumerate(self.weights):
        row_actuals = []
        for j,col_itm in enumerate(row):
          pass
          # item_res = A number
          # [i][j] 
          # quadrant = input_shape[x:x+x_sz][y:y+y_sz]
          # quad = self.extract_quadrant(self.source_index, resource_data.shape, coll_sgmnt.shape)
          # actuals = quad * coll_sgmnt.collection_chances * coll_sgmnt.weights #* coll_sgmnt.fill_shape
          # loop_through_array(2d) and collect actuals from each expected index
          # row_actuals.append()
        actuals.append(row_actuals)
    else:
      # loop_through_array(1d) and collect actuals from each expected index
      # quadrant = input_shape[x:x+x_sz]
      # quad = self.extract_quadrant(self.source_index, resource_data.shape, coll_sgmnt.shape)
      for i,row in enumerate(resource_data):
        pass
        # actuals = quad * coll_sgmnt.collection_chances * coll_sgmnt.weights #* coll_sgmnt.fill_shape
    return array(actuals)
