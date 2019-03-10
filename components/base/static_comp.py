class StaticComp:

  def __init__(self, itm_id, ctg):
    self.itm_id = itm_id
    self.ctg = ctg

  def get_id(self):
    return self.itm_id

  def get_ctg(self):
    return self.ctg

  def set_id(self, itm_id):
    self.itm_id = itm_id

  def set_ctg(self, ctg):
    self.ctg = ctg