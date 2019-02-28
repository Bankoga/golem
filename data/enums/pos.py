from enum import Enum

class ComponentType(Enum):
  MATRIX = 1
  HOOK = 2
  GROUP = 3
  PACKAGER = 4
  INSTRUCTION = 5

class Floor(Enum):
  CELLAR = 1
  BASEMENT = 2
  ARCHIVE = 3
  MAIN = 4
  ATTIC = 5

  def describe(self):
    return 'Matrix section', self.name