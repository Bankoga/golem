from abc import abstractmethod
from data.enums.pos import ComponentType

class Component:
  def __init__(self, component_id,component_type, ctg_type=None):
    """
    component_id : the semantic key used as reference for the component object
    component_type : the semantic key used as reference for the components operational level within the matrix
    ctg__type : the semantic key used as reference for the components operational level specific group type
    """
    self.ctg_type = ctg_type
    self.itm_id = component_id
    self.op_lvl = ComponentType(component_type)
    self._built_ = False
    self.var = None

  def get_id(self):
    return self.itm_id

  def get_ctg(self):
    return self.ctg_type

  def get_level(self):
    return self.op_lvl

  @abstractmethod
  def build(self, data):
    if not self._built_:
      self.var = data
      self._built_ = True
    # else:
    #   self.reset()
  
  def is_built(self):
    return self._built_

  @abstractmethod
  def operate(self):
    if not self._built_:
      raise RuntimeError('The component is not ready for operation!')
  
  @abstractmethod
  def update(self, new_data=None):
    if self._built_:
      self._built_ = False
      self.var = new_data

  @abstractmethod
  def reset(self):
    if self._built_:
      self._built_ = False
      self.var = None