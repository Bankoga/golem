from components.enums.pos import Floor, CtgType, Dimension

class Pos:
  def __init__(self,op_lvl=-1,floor=Floor.WAREHOUSE,x=-1,y=-1,z=-1,r=-1,c=-1):
    self.op_lvl = op_lvl
    self.floor = floor
    self.x = x
    self.y = y
    self.z = z
    self.r = r
    self.c = c
    self._pos_tup_ = None
  
  def get_hash(self):
    if self._pos_tup_ is None:
      self._pos_tup_ = (self.op_lvl,self.floor,self.x,self.y,self.z,self.r,self.c)
    return hash(self._pos_tup_)
  
  def get_dim_value(self,dim_key):
    if dim_key is Dimension.OP_LVL:
      return self.op_lvl
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

def diff_addrs(addr_a, addr_b):
  diff_mag = 0
  if addr_a.golem != addr_b.golem:
    diff_mag = diff_mag + 70
  if addr_a.matrix != addr_b.matrix:
    diff_mag = diff_mag + 60
  if addr_a.func_set != addr_b.func_set:
    diff_mag = diff_mag + 50
  if addr_a.stage != addr_b.stage:
    diff_mag = diff_mag + 40
  if addr_a.group != addr_b.group:
    diff_mag = diff_mag + 30
  if addr_a.packager != addr_b.packager:
    diff_mag = diff_mag + 20
  if addr_a.instruction != addr_b.instruction:
    diff_mag = diff_mag + 10
  if addr_a.channel != addr_b.channel:
    diff_mag = diff_mag + 1
  return diff_mag