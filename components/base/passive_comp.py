from components.base.static_comp import StaticComp

class PassiveComp(StaticComp):

  def __init__(self, var, **kwargs):
    super().__init__(kwargs['item_id'],kwargs['ctg'])
    self.var = var

  @property
  def var(self):
    return self.__var

  @var.setter
  def var(self, var):
    self.__var = var