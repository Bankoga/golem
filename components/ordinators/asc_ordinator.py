from components.ordinators.ordinator import Ordinator

class AscOrdinator(Ordinator):
  """
  Responsible for handling inter/intra matrix direction interpretation
  """
  def __init__(self):
    super().__init__("asc")
  
  def get_ord_index(self, index, size):
    self.ordinal_direction
  

class AscOrdinatorBuilder:
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = AscOrdinator()
    return self._instance