# from components.base.dynamic_comp import DynamicComp
from components.base.component import Component
from components.enums.prop_types import PackType,RsrcType,FieldType
from chainer import Variable

class Package(Component):
  """
  For all intents and purposes, a package is a mail package
  It has the following properties
    - sender
    - recipient
    - type
    - shape : valid field type TODO: revisit shape
    - var : chainer variable
  there are two types of data packs planned currently
  - overlayed
    - is to be processed by itself as a full shape
  - aggregated
    - gets joined with others using a guaranteed ordering to produce a full shape to be processed
  
  eventually, are package shapes going to be chainer variables?
  """
  def __init__(self, meld,sender_address):
    self.meld_tuple = meld.split(';')
    self.sender = sender_address
    self.read_data()
    super().__init__(self.get_meld(),self.ctg_type.get_component_type(),self.ctg_type)
  
  def read_data(self):
    self.address=self.meld_tuple[0]
    self.resource=RsrcType.UNSET
    self.shape = FieldType.UNSET
    self.ctg_type = PackType.UNSET
    if len(self.meld_tuple) > 1 and self.meld_tuple[1] and self.meld_tuple[1] in RsrcType:
      self.resource = self.meld_tuple[1]
      if self.meld_tuple[2] != 0 and self.meld_tuple[2] in PackType:
        self.ctg_type=PackType(self.meld_tuple[2])
        if len(self.meld_tuple) >3 and self.meld_tuple[3] and self.meld_tuple[3] in FieldType:
          self.shape=FieldType(self.meld_tuple[3])
    self.var = None

  def get_meld(self):
      return f'{self.sender};{self.address};{self.resource};{self.ctg_type};{self.shape}'

  def operate(self):
    super().operate()

  def build(self, data=None):
    super().build(data)

  def update(self, new_addr):
    self.address = new_addr
    self._built_ = False
    self.var = None

  def reset(self):
    super().reset()

  def __eq__(self, other):
    return self.__dict__ == other.__dict__
  
  def __lt__(self,other):
    return self.get_meld() < other.get_meld()
  
  def __le__(self,other):
    return self.get_meld() <= other.get_meld()
  
  def __gt__(self,other):
    return self.get_meld() > other.get_meld()
  
  def __ge__(self,other):
    return self.get_meld() >= other.get_meld()