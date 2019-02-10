from utils.datapack import *

class Melder:
  def __init__(self):
    pass

  def eval_full(self, meld):
    parts=meld.split(",")
    return Datapack(tuple(parts))

  def eval_meld(self, meld):
    return meld
    
  def eval_melds(self):
    pass
