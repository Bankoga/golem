from enum import Enum, auto

class AutoName(Enum):
  def _generate_next_value_(name,start,count,last_values):
    return name

class PackType(Enum):
  UNSET = 1
  AGGREGATE = 2
  OVERLAY = 9

class RsrcType(Enum):
  UNSET = 1
  ENERGY = 2
  INHIBITOR = 3

class FieldType(Enum):
  UNSET = 1
  TEST_INPUT = 2
  TEST_OUTPUT = 3

class GroupType(Enum):
  UNSET = 1
  SENSOR = 101
  CORTICAL = 201
  GATEWAY = 202

class HookType(Enum):
  UNSET = 1
  UNI = 101
  BI = 102
  RECIP = 103

class RuleType(Enum):
  UNSET = 1
  CELL = 100
  FW_FUNC = 500

# (PackType|RsrcType|FieldType|GroupType|HookType|RuleType)