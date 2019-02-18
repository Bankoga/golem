from data.axioms.pos_maps import floor_order
class Ordinator():

  """
  Responsible for handling inter/intra matrix direction interpretation
  """
  def __init__(self, direction):
    self.ordinal_direction = direction
    
  def get_id(self):
    return self.ordinal_direction
  
  def get_direction(self):
    return self.ordinal_direction
  
  def get_ord_index(self, ind, sz):
    if ind < sz:
      return ind
    else:
      return 0

  # def get_floor_index(self, floor_id):
  #   return floor_order.index(floor_id)
