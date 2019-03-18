from components.base.workers.worker_comp import WorkerComp

class ProducerComp(WorkerComp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)