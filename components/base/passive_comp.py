from components.base.static_comp import StaticComp

class PassiveComp(StaticComp):
  def __init__(self, var, **kwargs):
    super().__init__(kwargs['item_id'],kwargs['ctg'])
    self.set_var(var)

  def set_var(self, var):
    self.var = var

  def get_var(self):
    return self.var