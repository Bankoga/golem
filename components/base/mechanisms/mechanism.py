from abc import abstractmethod

from components.base.buildable_comp import BuildableComp
from components.matrix.address_registry import AddressRegistry

class Mechanism(BuildableComp):
  def __init__(self, *args,**kwargs):
    super().__init__(*args, **kwargs)

  def set_defaults(self):
    self.__is_registered = False
    self.__address = None
    return super().set_defaults()

  @property
  def registry(self):
    return self.var[0]

  @registry.setter
  def registry(self, value):
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
    self.registry.add_item(self.reg_item)
    self.__is_registered = True

  def operate(self,*args,**kwargs):
    if not self.is_registered:
      raise RuntimeError('An unregistered worker type cannot operate!')
    else:
      return self.operation_details(*args, **kwargs)

  def operation_details(self,*args,**kwargs):
    res = []
    for arg in args:
      if type(arg) is iter:
        res.append(arg.any())
      else:
        res.append(not arg is False)
    return res
  
  def build_details(self, *args, **kwargs):
    super().build_details(*args, **kwargs)
    if 'address' in kwargs:
      self.register(kwargs['address'])