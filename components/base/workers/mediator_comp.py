from components.base.workers.worker_comp import WorkerComp

class MediatorComp(WorkerComp):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  @property
  def address_registry(self):
    return self.registry

  @address_registry.setter
  def address_registry(self, value):
    raise RuntimeError('Cannot set address registry!')

  @property
  def channel_registry(self):
    return self.var[1]

  @channel_registry.setter
  def channel_registry(self, value):
    raise RuntimeError('Cannot set channel registry!')