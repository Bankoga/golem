from utils.validators.pos_validators import is_valid_ctg
from utils.validators.prop_validators import is_valid_id

class StaticComp:

  def __init__(self, itm_id, ctg):
    if not is_valid_ctg(ctg):
      raise ValueError('INVALID CATEGORY!')
    elif not is_valid_id(itm_id):
      raise ValueError('INVALID ID!')
    else:
      self.itm_id = itm_id
      self.ctg = ctg

  def get_id(self):
    return self.itm_id

  def get_ctg(self):
    return self.ctg

  def set_id(self, itm_id):
    if not is_valid_id(itm_id):
      raise ValueError('INVALID ID!')
    else:
      self.itm_id = itm_id

  def set_ctg(self, ctg):
    if not is_valid_ctg(ctg):
      raise ValueError('INVALID CATEGORY!')
    else:
      self.ctg = ctg