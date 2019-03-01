from enum import Enum, auto

from data.enums.pos import ComponentLevel

class AutoName(Enum):
  def _generate_next_value_(name,start,count,last_values): # pylint: disable=no-self-argument
    return name

class PackType(Enum):
  UNSET = 1
  AGGREGATE = 2
  OVERLAY = 9
  def get_component_type(self):
    return ComponentLevel.PACKAGE

class RsrcType(Enum):
  UNSET = 1
  ENERGY = 2
  INHIBITOR = 3
  def get_component_type(self):
    return ComponentLevel.DATA

class FieldType(Enum):
  UNSET = 1
  TEST_INPUT = 2
  TEST_OUTPUT = 3
  def get_component_type(self):
    return ComponentLevel.DATA

class GroupType(Enum):
  UNSET = 1
  SENSOR = 101
  CORTICAL = 201
  GATEWAY = 202
  def get_component_type(self):
    return ComponentLevel.GROUP

class HookType(Enum):
  UNSET = 1
  UNI = 101
  BI = 102
  RECIP = 103
  def get_component_type(self):
    return ComponentLevel.HOOK

class RuleType(Enum):
  UNSET = 1
  CELL = 100
  FW_FUNC = 500
  def get_component_type(self):
    return ComponentLevel.INSTRUCTION

# (PackType|RsrcType|FieldType|GroupType|HookType|RuleType)