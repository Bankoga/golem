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

def diff_lineages(lineage_a, lineage_b):
  diff_mag = 0
  if lineage_a.golem != lineage_b.golem:
    diff_mag = diff_mag + 70
  if lineage_a.matrix != lineage_b.matrix:
    diff_mag = diff_mag + 60
  if lineage_a.func_set != lineage_b.func_set:
    diff_mag = diff_mag + 50
  if lineage_a.stage != lineage_b.stage:
    diff_mag = diff_mag + 40
  if lineage_a.group != lineage_b.group:
    diff_mag = diff_mag + 30
  if lineage_a.packager != lineage_b.packager:
    diff_mag = diff_mag + 20
  if lineage_a.instruction != lineage_b.instruction:
    diff_mag = diff_mag + 10
  if lineage_a.channel != lineage_b.channel:
    diff_mag = diff_mag + 1
  return diff_mag