from numpy import ones

from components.base.passive_comp import PassiveComp

from components.enums.pos import CtgType

class ConvShape(PassiveComp):

  """
  While ConvShapes are components, we need to break up the component base class into two types
  Why one asks? Because some components require building, and others don't
  Some require updates, but no builds, some require both, some are static
  the position is relative to its parents X,Y (or row/column) index within stage Z
  """

  def __init__(self,source_id,source_index,f_shape,s_shape=None, **kwargs):
    kwargs['ctg']=CtgType.DATA
    super().__init__(source_id,source_index,f_shape,s_shape,ones(f_shape), **kwargs)

  @property
  def weights(self):
    return self.var[4]
  
  @weights.setter
  def weights(self, value):
    self.setter_error()

  @property
  def filter_shape(self):
    return self.var[2]
  
  @filter_shape.setter
  def filter_shape(self, value):
    self.setter_error()

  @property
  def spacing_shape(self):
    return self.var[3]
  
  @spacing_shape.setter
  def spacing_shape(self, value):
    self.setter_error()
  
  @property
  def source_index(self):
    return self.var[1]
  
  @source_index.setter
  def source_index(self, value):
    self.setter_error()

  @property
  def source_id(self):
    return self.var[0]
  
  @source_id.setter
  def source_id(self, value):
    self.setter_error()
