from data.axioms.configs import id_pattern
from data.axioms.enums import HookType,PackType,RsrcType,FieldType
from utils.datapack import Datapack
import re

class Hook(Datapack):
  """
  For all intents and purposes, a hook is a trigger for building datapacks
  Hooks have these additional properties to datapack properties in the proc configs
    - hook_id
    - direction: to/from
    - target: the module to use in the blank spots in the datapack production rule
    - type simple dict of all hook ids to hook_types used in the golem type matrix
  hook_bases are currently defined at the lowest level, in proc groups
  A hook base is the mdl whch srvs as the anchor for cnnctng mdls usng HookType of HookId
  
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
    self._id_updated_ = False
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

  def update_id(self,container_id):
    if (not self._id_updated_ and (not '\n' in container_id) and container_id and re.search(id_pattern, container_id)):
      new_id = f'{container_id}-{self.hook_id}'
      self.hook_id = new_id
      self._id_updated_ = True

  def process_hook(self):
    pass