from utils.cardinators.cardinator import Cardinator

class DscCardinator(Cardinator):
  """
  Responsible for handling inter/intra matrix direction interpretation
  """
  def __init__(self):
    super().__init__("dsc")
  
  def get_card_index(self, index, size):
    if index >= 0 and index < size:
      return size - index - 1
    else:
      raise ValueError("The ord index is invalid")

class DscCardinatorBuilder:
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = DscCardinator()
    return self._instance