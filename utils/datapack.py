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
  def __init__(self, meld_tuple,module_id=''):
    self._read_data_(meld_tuple)
    self._format_address_(module_id)
  
  def _read_data_(self,meld_tuple):
    self.address=meld_tuple[0]
    self.resource=meld_tuple[1]
    self.shape=meld_tuple[2]
    self.type = PackTypes[meld_tuple[3]]

  def _format_address_(self,module_id):
    pass