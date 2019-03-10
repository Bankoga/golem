from utils.validators.pos_validators import is_valid_ctg
from utils.validators.prop_validators import is_valid_id

class StaticComp:

  def __init__(self, item_id, ctg):
    self.set_id(item_id)
    self.set_ctg(ctg)

  def get_id(self):
    return self.item_id

  def get_ctg(self):
    return self.ctg

  def set_id(self, item_id):
    if not is_valid_id(item_id):
      raise ValueError('INVALID ID!')
    else:
      self.item_id = item_id

  def set_ctg(self, ctg):
    if not is_valid_ctg(ctg):
      raise ValueError('INVALID CATEGORY!')
    else:
      self.ctg = ctg