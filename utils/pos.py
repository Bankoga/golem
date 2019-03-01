class Pos:
  def __init__(self,s=-1,x=-1,y=-1,z=-1):
    self.s = s
    self.x = x
    self.y = y
    self.z = z
    self._pos_tup = None
  
  def get_hash(self):
    if self._pos_tup is None:
      self._pos_tup = (self.s,self.x,self.y,self.z)
    return hash(self._pos_tup)