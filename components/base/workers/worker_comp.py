from components.base.static_comp import StaticComp

class WorkerComp(StaticComp):
  def __init__(self, **kwargs):
    super().__init__(kwargs['item_id'],kwargs['ctg'])