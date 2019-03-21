from components.matrix.matrix_comp import MatrixComp

from utils.validators.matrix import reg_item_check

class Registry(MatrixComp):
  def __init__(self, **kwargs):
    super().__init__({}, **kwargs)

  @property
  def registry(self):
    return self.var[0]

  @registry.setter 
  def registry(self, value):
   raise RuntimeError('Cannot set registry directly!')

  def add_item(self, new_item):
    if reg_item_check(new_item):
      self._dup_safe_add(new_item)
    else:
      raise RuntimeError('Cannot add invalid item to registry!')
  
  def _dup_safe_add(self, new_item):
    if new_item['reg_id'] in self.registry:
      raise RuntimeError('Cannot add duplicate item to registry!')
    self.registry[new_item['reg_id']] = new_item

  def remove_item(self, reg_id):
    if not reg_id in self.registry:
      raise RuntimeError('Cannot remove what does not exist!')
    else:
      del self.registry[reg_id]
  
  def get_item(self, reg_id):
    return self.registry[reg_id]

# def subclasses(cls, registry=None):
#   if registry is None:
#     registry = set()

#   subs = cls.__subclasses__()

#   for sub in subs:
#     if sub in registry:
#       return
#     registry.add(sub)
#     yield sub
#     for sub in subclasses(sub, registry):
#       yield sub


# REGISTRY = {cls.__name__: cls for cls in subclasses(WorkerComp)}

# def register_class(target_class):
#   REGISTRY[target_class.__name__] = target_class