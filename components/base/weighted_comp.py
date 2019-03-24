from components.base.static_comp import StaticComp

class WeightedComp(StaticComp):

  def __init__(self, *args, **kwargs):
   super().__init__(*args, **kwargs)
  
  def set_defaults(self):
    self.set_weighted_defaults()
    return super().set_defaults()
  
  def set_weighted_defaults(self, shape=tuple([]),weights=[]):
    self.__is_locked = False
    self.shape = shape
    self.weights = weights
   
  @property
  def weights(self):
    return self.__weights
  
  @weights.setter
  def weights(self, value):
    if self.is_locked:
      raise RuntimeError('Can not change weights of a locked component!')
    else:
      self.__weights = value
    
  @property
  def shape(self):
    return self.__shape
  
  @shape.setter
  def shape(self, value):
    if self.is_locked:
      raise RuntimeError('Can not change shape of a locked component!')
    else:
      self.__shape = value
      self.__num_dim_of_mass = len(self.__shape)
    
  @property
  def num_dim_of_mass(self):
    return self.__num_dim_of_mass
  
  @num_dim_of_mass.setter
  def num_dim_of_mass(self, value):
    raise RuntimeError('Can not set the num dim of mass! It is derived from the shape!')
  
  @property
  def is_locked(self):
    return self.__is_locked
  
  @is_locked.setter
  def is_locked(self, value):
    raise RuntimeError('Toggle the lock status via toggle lock instead!')
  
  def toggle_lock(self):
    if self.is_locked:
      self.__is_locked = False
    else:
      self.__is_locked = True