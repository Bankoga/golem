from enum import Enum, auto
from components.enums.misc_enum import AutoName

class QuantChange(AutoName):
  NONE = auto()
  BASE = auto()
  LOW = auto()
  MEDIUM = auto()
  HIGH = auto()

class QuantDuration(AutoName):
  INSTANT = auto()
  BRIEF = auto()
  MODERATE = auto()
  PERSISTENT = auto()
  EXTENDED = auto()
  PROLONGED = auto()
  CONTINUOUS = auto()