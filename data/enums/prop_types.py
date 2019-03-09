from enum import Enum, auto

from data.enums.pos import ComponentType

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
    return ComponentType.HOOK

class FuncSetType(Enum):
  UNSET = 1
  SENSOR = 101
  CORTICAL = 201
  GATEWAY = 202
  def get_component_type(self):
    return ComponentType.FSET
  def sub_group(self):
    if 100 < self.value and self.value < 200:
      return SuperSet.CODER
    elif 200 < self.value and self.value < 300:
      return SuperSet.PROC
    else:
      return SuperSet.UNSET

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
    return ComponentType.GROUP

class PackagerType(Enum):
  UNSET = 1
  CELL = 100
  FW_FUNC = 500
  def get_component_type(self):
    return ComponentType.PACKAGER

class RuleType(Enum):
  UNSET = 1
  CONV = 100
  METHOD = 500
  def get_component_type(self):
    return ComponentType.INSTRUCTION

# (PackType|RsrcType|FieldType|FuncSetType|HookType|RuleType)

class PackType(Enum):
  UNSET = 1
  AGGREGATE = 2
  OVERLAY = 9
  def get_component_type(self):
    return ComponentType.PACKAGE

class RsrcType(Enum):
  UNSET = 1
  ENERGY = 2
  INHIBITOR = 3
  def get_component_type(self):
    return ComponentType.DATA

class FieldType(Enum):
  UNSET = 1
  TEST_INPUT = 2
  TEST_OUTPUT = 3
  def get_component_type(self):
    return ComponentType.DATA
