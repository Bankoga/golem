from data.axioms.enums import PackType,RsrcType,FieldType

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
  def __init__(self, meld,sender_address):
    self.meld_tuple = meld.split(':')
    self.sender = sender_address
    self.read_data()
    self._format_address_()
  
  def read_data(self):
    self.address=self.meld_tuple[0]
    self.resource=RsrcType.UNSET
    if self.meld_tuple[1] in RsrcType:
      self.resource = self.meld_tuple[1]
    shp = FieldType.UNSET
    typ = PackType.UNSET
    if self.meld_tuple[2] != 0 and self.meld_tuple[2] in PackType:
      typ = PackType(self.meld_tuple[2])
      if len(self.meld_tuple) >3 and self.meld_tuple[3] and self.meld_tuple[3] in FieldType:
        shp=FieldType(self.meld_tuple[3])
    self.type = typ
    self.shape=shp

  def _format_address_(self):
    pass