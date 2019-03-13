from components.enums.pos import floor_order
class Cardinator():

  """
  Responsible for handling inter/intra matrix direction interpretation
  """
  def __init__(self, direction):
    self.cardinal_direction = direction
    
  def get_id(self):
    return self.cardinal_direction
  
  def get_direction(self):
    return self.cardinal_direction
  
  def get_card_index(self, index, size):
    if index >= 0 and index < size:
      return index
    else:
      raise ValueError("The ord index is invalid")
  

  # def get_floor_index(self, floor_id):
  #   return floor_order.index(floor_id)
