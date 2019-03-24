from components.base.static_comp import StaticComp

class WeightedComp(StaticComp):

  def __init__(self, *args, **kwargs):
   super().__init__(kwargs['label'], kwargs['ctg'])