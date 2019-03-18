from components.base.workers.worker_comp import WorkerComp

class MediatorComp(WorkerComp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

# TODO: every mediator needs to receive a hook to the registry so that it can be used to create channels and register things