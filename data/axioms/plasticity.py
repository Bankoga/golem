from enum import Enum, auto

class AutoName(Enum):
  def _generate_next_value_(name, start, count, last_values):
    return name

class QuantChange(AutoName):
  NONE = auto()
  BASE = auto()
  LOW = auto()
  MEDIUM = auto()
  HIGH = auto()

class QuantDuration(AutoName):
  NONE = auto()
  INSTANT = auto()
  BRIEF = auto()
  PERSISTENT = auto()
  EXTENDED = auto()
  PROLONGED = auto()
  CONTINUOUS = auto()