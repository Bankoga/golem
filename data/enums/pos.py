from enum import Enum, auto
from data.enums.misc_enum import AutoName

class Dimension(AutoName):
  OP_LVL = auto()
  FLOOR = auto()
  LENGTH = auto()
  WIDTH = auto()
  HEIGHT = auto()
  ROW = auto()
  COLUMN = auto()


class DimensionallyOrdered(Enum):
  def __init__(self,pos,dimension):
    self.pos = pos
    self.dimension = dimension

class ComponentType(Enum):
  MATRIX = auto()
  HOOK = auto()
  SET = auto()
  GROUP = auto()
  PACKAGER = auto()
  INSTRUCTION = auto()
  PACKAGE = auto()
  DATA = auto()

class Floor(Enum):
  WAREHOUSE = auto()
  CELLAR = auto()
  BASEMENT = auto()
  ARCHIVE = auto()
  MAIN = auto()
  ATTIC = auto()

  def describe(self):
    return 'Matrix section', self.name


# class CardinalX(Enum):
#   UNSET = 1
# class CardinalY(Enum):
#   UNSET = 1
# class CardinalZ(Enum):
#   UNSET = 1
#   BELOW = 100
#   BETWEEN = 200
#   CENTER = 201
#   MIDDLE = 202
#   ABOVE = 300