from data.axioms.enums import HookType,PackType,RsrcType,FieldType
from utils.datapack import Datapack

class Hook(Datapack):
  """
  For all intents and purposes, a hook is a trigger for building datapacks
  Hooks have the additional properties to datapack properties
    - hook_id
    - direction: to/from
    - target: the module to use in the blank spots in the datapack production rule
  """
  def __init__(self, meld):
    self.meld_tuple = meld.split(';')
    self.read_data()
  
  def read_data(self):
    # self.hook_id=self.meld_tuple[0]
    # self.hook_type
    # self.resource=RsrcType.UNSET
    # self.shape = FieldType.UNSET
    # self.type = PackType.UNSET
    # if len(self.meld_tuple) > 1 and self.meld_tuple[1] and self.meld_tuple[1] in RsrcType:
    #   self.resource = self.meld_tuple[1]
    #   if self.meld_tuple[2] != 0 and self.meld_tuple[2] in PackType:
    #     self.type=PackType(self.meld_tuple[2])
    #     if len(self.meld_tuple) >3 and self.meld_tuple[3] and self.meld_tuple[3] in FieldType:
    #       self.shape=FieldType(self.meld_tuple[3])
  
    self.hook_id = self.meld_tuple[0]
    self.hook_type = HookType.UNSET
    self.resource = RsrcType.UNSET
    self.type = PackType.UNSET
    self.shape = FieldType.UNSET
    if self.meld_tuple[1] and self.meld_tuple[1] in HookType:
      self.hook_type=HookType(self.meld_tuple[1])
    self.address=self.meld_tuple[2]
    if len(self.meld_tuple)>3 and self.meld_tuple[3] and self.meld_tuple[3] in RsrcType:
      self.resource=RsrcType(self.meld_tuple[3])
    if len(self.meld_tuple)>4 and self.meld_tuple[4] and self.meld_tuple[4] in PackType:
      self.type=PackType(self.meld_tuple[4])
    if len(self.meld_tuple)>5 and self.meld_tuple[5] and self.meld_tuple[5] in FieldType:
      self.shape=self.meld_tuple[5]


  def process_hook(self):
    pass