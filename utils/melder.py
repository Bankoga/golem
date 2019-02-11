from utils.datapack import *

class Melder:
  def __init__(self):
    pass

  def eval_meld(self, meld):
    """
      Produces one or more datapacks based on the meld format
      There are ? formats:
      - ?
      How do we identify each format?
    """
    # case 
    parts=meld.split(",")
    return Datapack(tuple(parts))

  def eval_melds(self):
    pass
