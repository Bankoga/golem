from components.base.passive_comp import PassiveComp

class Segment(PassiveComp):
  def __init__(self, address, source_index, fill_shape,**kwargs):
    super().__init__(address,source_index,fill_shape,**kwargs)
  
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
  