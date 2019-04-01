from components.base.static_comp import StaticComp

class Segment(StaticComp):
  def __init__(self, *args,**kwargs):
    super().__init__(**kwargs)
    self.__residence_address = kwargs['residence_address']
    self.__source_address = kwargs['source_address']
    self.__source_index = kwargs['source_index']
    self.__fill_shape = kwargs['fill_shape']
  
  @property
  def residence_address(self):
    return self.__residence_address
  @residence_address.setter
  def residence_address(self, value):
    self.setter_error()

  @property
  def source_address(self):
    return self.__source_address
  @source_address.setter
  def source_address(self, value):
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
    self.__fill_shape = value

  def setter_error(self):
    raise RuntimeError('Can not set property of segment!')
  