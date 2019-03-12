from components.matrix.matrix_comp import MatrixComp

class Registry(MatrixComp):
  def __init__(self, **kwargs):
    super().__init__({}, **kwargs)



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