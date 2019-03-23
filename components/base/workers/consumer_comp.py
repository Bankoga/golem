from components.base.workers.worker_comp import WorkerComp

class ConsumerComp(WorkerComp):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)