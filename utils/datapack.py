class Datapack:
  def __init__(self, meld_tuple):
    self.address=meld_tuple[0]
    self.resource=meld_tuple[1]
    self.shape=meld_tuple[2]
    self.type = f'{self.address}:{self.resource}'
    """
    there are two types of data packs planned currently
    - overlayed
      - is to be processed by itself as a full shape
    - aggregated
      - gets joined with others using a guaranteed ordering to produce a full shape to be processed