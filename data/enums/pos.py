from enum import Enum, auto
from data.enums.misc_enum import AutoName

def Dimensions(AutoName):
  P = auto()
  O = auto()
  S = auto()
  X = auto()
  Y = auto()
  Z = auto()

class DimensionallyOrdered(Enum):
  def __init__(self,pos,dimension):
    self.pos = pos
    self.dimension = dimension

class ComponentLevel(Enum):
  MATRIX = 1
  HOOK = 2
  GROUP = 3
  PACKAGER = 4
  INSTRUCTION = 5
  PACKAGE = 6
  DATA = 7

class Floor(Enum):
  CELLAR = 1
  BASEMENT = 2
  ARCHIVE = 3
  MAIN = 4
  ATTIC = 5

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