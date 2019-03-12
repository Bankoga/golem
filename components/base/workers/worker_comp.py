from abc import abstractmethod

from components.base.static_comp import StaticComp

class WorkerComp(StaticComp):
  def __init__(self, **kwargs):
    super().__init__(kwargs['item_id'],kwargs['ctg'])

  @abstractmethod
  def register(self):
    raise RuntimeError('An unimplemented worker type cannot register')
  
  @abstractmethod
  def operate(self):
    raise RuntimeError('An unimplemented worker type cannot operate')