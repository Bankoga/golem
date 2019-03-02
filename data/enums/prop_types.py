from enum import Enum, auto

from data.enums.pos import ComponentType

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

class SetType(Enum):
  UNSET = 1
  SENSOR = 101
  CORTICAL = 201
  GATEWAY = 202
  def get_component_type(self):
    return ComponentType.SET
  def sub_group(self):
    if 100 < self.value and self.value < 200:
      return SuperSet.CODER
    elif 200 < self.value and self.value < 300:
      return SuperSet.PROC
    else:
      return SuperSet.UNSET

class SuperSet(Enum):
  UNSET = 1
  CODER = 2
  PROC = 3


class NodeType(Enum):
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

# (PackType|RsrcType|FieldType|SetType|HookType|RuleType)

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
