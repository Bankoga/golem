from abc import abstractmethod

from components.base.static_comp import StaticComp

class WorkerComp(StaticComp):
  def __init__(self, **kwargs):
    super().__init__(kwargs['label'],kwargs['ctg'])
    self.__is_registered = False
    self.__address = None

  @property
  def reg_item(self):
    return {
      'reg_id': self.label,
      'address': self.address
    }
  
  @reg_item.setter
  def reg_item(self, value):
    raise RuntimeError('The reg item cannot be set!')

  @property
  def address(self):
    return self.__address

  @address.setter
  def address(self, value):
    if self.is_registered:
      raise RuntimeError('The address cannot be changed after registration!')
    else:
      self.__address = value

  @property
  def is_registered(self):
    return self.__is_registered
  
  @is_registered.setter
  def is_registered(self, value):
    raise RuntimeError('This property cannot be set by the user!')

  @abstractmethod
  def register(self, address, registry):
    self.__address = address
    registry.add_item(self.reg_item)

    self.__is_registered = True
  
  @abstractmethod
  def operate(self):
    if not self.is_registered:
      raise RuntimeError('An unregistered worker type cannot operate!')
    else:
      pass
      # ?