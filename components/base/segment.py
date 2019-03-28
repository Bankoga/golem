from components.base.static_comp import StaticComp

class Segment(StaticComp):
  def __init__(self, address, source_index, fill_shape,**kwargs):
    super().__init__(**kwargs)
    self.__address = address
    self.__source_index = source_index
    self.__fill_shape = fill_shape
  
  @property
  def address(self):
    return self.__address
  @address.setter
  def address(self, value):
    self.setter_error()
    
  @property
  def source_index(self):
    return self.__source_index
  @source_index.setter
  def source_index(self, value):
    self.setter_error()

  @property
  def fill_shape(self):
    return self.__fill_shape
  @fill_shape.setter
  def fill_shape(self, value):
    self.setter_error()

  def setter_error(self):
    raise RuntimeError('Can not set property of segment!')
  