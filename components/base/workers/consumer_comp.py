from components.base.workers.worker_comp import WorkerComp

class ConsumerComp(WorkerComp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)