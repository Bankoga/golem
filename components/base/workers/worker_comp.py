from abc import abstractmethod

from components.base.active_comp import ActiveComp
from components.base.buildable_comp import BuildableComp
from components.matrix.address_registry import AddressRegistry

class WorkerComp(BuildableComp, ActiveComp):
  def __init__(self, *args,**kwargs):
    super().__init__(*args, **kwargs)
    self.__is_registered = False
    self.__address = None

  @property
  def reg_connection(self):
    return self.var[0]

  @reg_connection.setter
  def reg_connection(self, value):
    if type(value) == AddressRegistry:
      self.update(value)
    else:
      raise RuntimeError('Attempted to set an invalid reg connection!')

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
  def register(self, address, registry=None):
    self.__address = address
    self.reg_connection.add_item(self.reg_item)
    self.__is_registered = True

  @abstractmethod
  def operate(self):
    if not self.is_registered:
      raise RuntimeError('An unregistered worker type cannot operate!')
    else:
      pass
      # ?

  def build(self, *args, **kwargs):
    super().build(*args)
    if 'address' in kwargs:
      self.register(kwargs['address'])