from components.matrix.matrix_comp import MatrixComp

from utils.validators.matrix import reg_item_check

class Registry(MatrixComp):
  def __init__(self, **kwargs):
    super().__init__({}, **kwargs)

  def add_item(self, new_item):
    if reg_item_check(new_item):
      if new_item['reg_id'] in self.var:
        raise RuntimeError('Cannot add duplicate item to registry!')
      self.var[new_item['reg_id']] = new_item
    else:
      raise RuntimeError('Cannot add invalid item to registry!')
  
  def remove_item(self, reg_id):
    if not reg_id in self.var:
      raise RuntimeError('Cannot remove what does not exist!')
    else:
      del self.var[reg_id]
  
  def get_item(self, reg_id):
    return self.var[reg_id]

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