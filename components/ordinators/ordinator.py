class Ordinator:

  """
  Responsible for handling inter/intra matrix direction interpretation
  """
  def __init__(self, direction):
    self.ordinal_direction = direction
    
  def get_id(self):
    return self.ordinal_direction
  
  @abstractmethod # pylint: disable=undefined-variable
  def get_ord_index(self, index, size):
    pass

