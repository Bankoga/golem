from components.packages.package import *

class Melder:
  # DIS BE A FACTORY YO!
  def __init__(self):
    pass

  def eval_meld(self, meld):
    """
      Produces one or more packages based on the meld format
      There are ? formats:
      - ?
      How do we identify each format?
    """
    # case 
    parts=meld.split(",")
    return Package(tuple(parts))

  def eval_melds(self):
    pass
