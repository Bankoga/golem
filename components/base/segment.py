from components.base.static_comp import StaticComp

class Segment(StaticComp):
  def __init__(self, *args,**kwargs):
    super().__init__(**kwargs)
    self.__residence_lineage = kwargs['residence_lineage']
    self.__source_lineage = kwargs['source_lineage']
    self.__source_index = kwargs['source_index']
    self.__fill_shape = kwargs['fill_shape']
  
  @property
  def residence_lineage(self):
    return self.__residence_lineage
  @residence_lineage.setter
  def residence_lineage(self, value):
    self.setter_error()

  @property
  def source_lineage(self):
    return self.__source_lineage
  @source_lineage.setter
  def source_lineage(self, value):
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
  