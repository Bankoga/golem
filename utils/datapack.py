from data.axioms.enums import PackTypes

class Datapack:
  """
  For all intents and purposes, a datapack is a mail package
  It has the following properties
    - sender
    - recipient
    - type
    - shape
  there are two types of data packs planned currently
  - overlayed
    - is to be processed by itself as a full shape
  - aggregated
    - gets joined with others using a guaranteed ordering to produce a full shape to be processed
  """
  def __init__(self, meld_tuple, pack_type):
    self.address=meld_tuple[0]
    self.resource=meld_tuple[1]
    self.shape=meld_tuple[2]
    self.type = PackTypes[pack_type]