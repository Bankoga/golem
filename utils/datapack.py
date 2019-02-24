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
  
  eventually, are datapack shapes going to be chainer variables?
  """
  def __init__(self, meld,sender_address):
    self.meld_tuple = meld.split(';')
    self.sender = sender_address
    self.read_data()
  
  def read_data(self):
    self.address=self.meld_tuple[0]
    self.resource=RsrcType.UNSET
    self.shape = FieldType.UNSET
    self.type = PackType.UNSET
    if len(self.meld_tuple) > 1 and self.meld_tuple[1] and self.meld_tuple[1] in RsrcType:
      self.resource = self.meld_tuple[1]
      if self.meld_tuple[2] != 0 and self.meld_tuple[2] in PackType:
        self.type=PackType(self.meld_tuple[2])
        if len(self.meld_tuple) >3 and self.meld_tuple[3] and self.meld_tuple[3] in FieldType:
          self.shape=FieldType(self.meld_tuple[3])

  def process_address(self):
    pass

  def __eq__(self, other):
    return self.__dict__ == other.__dict__