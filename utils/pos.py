from data.enums.pos import Floor, ComponentType, Dimension

class Pos:
  def __init__(self,comp_type,floor=Floor.WAREHOUSE,x=-1,y=-1,z=-1,r=-1,c=-1):
    if (comp_type not in ComponentType):
      raise ValueError('Pos requires a valid component type!')

    self.comp_type = comp_type
    self.floor = floor
    self.x = x
    self.y = y
    self.z = z
    self.r = r
    self.c = c
    self._pos_tup_ = None
  
  def get_hash(self):
    if self._pos_tup_ is None:
      self._pos_tup_ = (self.comp_type,self.floor,self.x,self.y,self.z,self.r,self.c)
    return hash(self._pos_tup_)
  
  def get_dim_value(self,dim_key):
    if dim_key is Dimension.OP_LVL:
      return self.comp_type.value
    elif dim_key is Dimension.FLOOR:
      return self.floor.value
    elif dim_key is Dimension.LENGTH:
      return self.x
    elif dim_key is Dimension.WIDTH:
      return self.y
    elif dim_key is Dimension.HEIGHT:
      return self.z
    elif dim_key is Dimension.ROW:
      return self.r
    elif dim_key is Dimension.COLUMN:
      return self.c
    else:
      raise ValueError('Please supply a valid dimension!')