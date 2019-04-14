from enum import Enum, auto

from components.enums.pos import CtgType

# TODO: eventually this will need to be refactored to ensure that most of these dicts only have one instance

class AutoName(Enum):
  def _generate_next_value_(name,start,count,last_values): # pylint: disable=no-self-argument
    return name

class HookType(Enum):
  UNSET = 1
  UNI = 101
  BI = 102
  RECIP = 103
  def get_component_type(self):
    return CtgType.HOOK

class ModuleType(Enum):
  UNSET = 1
  SENSOR = 101
  CORTICAL = 201
  GATEWAY = 202
  def get_component_type(self):
    return CtgType.MODULE
  def sub_group(self):
    if 100 < self.value and self.value < 200:
      return SuperSet.CODER
    elif 200 < self.value and self.value < 300:
      return SuperSet.PROC
    else:
      return SuperSet.UNSET
  # DCGC = auto()
  # DCAGC = auto()
  # DFG = auto()
  # DFAGC = auto()
  # GLG = auto()
  # PS = auto()
  # TIC = auto()
  # ASLG = auto()
  # SLG = auto()
  # MLG = auto()
  # KBL = auto()

class SuperSet(Enum):
  UNSET = auto()
  CODER = auto()
  PROC = auto()
  def has_sub_type(self,set_type):
    if self is SuperSet.CODER:
      return 100 < set_type.value and set_type.value < 200
    elif self is SuperSet.PROC:
      return 200 < set_type.value and set_type.value < 300
    else:
      return False

class GroupType(Enum):
  ORGANO = auto()
  METALLO = auto()
  HYBRID = auto()
  def get_component_type(self):
    return CtgType.GROUP

class PackagerType(Enum):
  UNSET = 1
  CELL = 100
  FW_FUNC = 500
  def get_component_type(self):
    return CtgType.PACKAGER

class RuleType(Enum):
  UNSET = 1
  CONV = 100
  METHOD = 500
  def get_component_type(self):
    return CtgType.INSTRUCTION

# (ChannelType|ResourceType|FieldType|ModuleType|HookType|RuleType)

class ChannelType(Enum):
  UNSET = 1
  AGGREGATE = 2
  OVERLAY = 9
  def get_component_type(self):
    return CtgType.CHANNEL

class ResourceType(Enum):
  UNSET = 1
  ENERGIZER = 2
  INHIBITOR = 3
  def get_component_type(self):
    return CtgType.DATA

class FieldType(Enum):
  UNSET = 1
  TEST_INPUT = 2
  TEST_OUTPUT = 3
  def get_component_type(self):
    return CtgType.DATA
