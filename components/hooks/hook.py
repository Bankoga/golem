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
  def __init__(self, meld, hook_id="", hook_type=""):
    if not hook_id and not hook_type:
      mt = meld.split(';')
      self._set_hook_type_(mt[0],mt[1])
      self.meld_tuple = mt[2:]
    else:
      self._set_hook_type_(hook_id,hook_type)
      self.meld_tuple = meld.split(';')
    self.read_data()
  
  def _set_hook_type_(self, hook_id, hook_type):
    self.hook_id = hook_id
    self.hook_type = HookType.UNSET
    if hook_type and hook_type in HookType:
      self.hook_type=HookType(hook_type)

  def read_data(self):
    self.resource = RsrcType.UNSET
    self.type = PackType.UNSET
    self.shape = FieldType.UNSET
    self.address=self.meld_tuple[0]
    if len(self.meld_tuple)>1 and self.meld_tuple[1] and self.meld_tuple[1] in RsrcType:
      self.resource=RsrcType(self.meld_tuple[1])
    if len(self.meld_tuple)>2 and self.meld_tuple[2] and self.meld_tuple[2] in PackType:
      self.type=PackType(self.meld_tuple[2])
    if len(self.meld_tuple)>3 and self.meld_tuple[3] and self.meld_tuple[3] in FieldType:
      self.shape=self.meld_tuple[3]


  def process_hook(self):
    pass