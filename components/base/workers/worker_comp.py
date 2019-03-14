from abc import abstractmethod

from components.base.static_comp import StaticComp

class WorkerComp(StaticComp):
  def __init__(self, **kwargs):
    super().__init__(kwargs['item_id'],kwargs['ctg'])
    self.__is_registered = False

  @property
  def is_registered(self):
    return self.__is_registered
  
  @is_registered.setter
  def is_registered(self, value):
    raise RuntimeError('This property cannot be set by the user!')

  @abstractmethod
  def register(self):
    raise RuntimeError('An unimplemented worker type cannot register!')
  
  @abstractmethod
  def operate(self):
    raise RuntimeError('An unimplemented worker type cannot operate!')