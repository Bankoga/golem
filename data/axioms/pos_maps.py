from enum import Enum

package_map = {
  'core': 'main',
  'framework': 'basement',
  'regulator': 'basement',
  'shell': 'cellar',
  'memory': 'archive',
  'dm': 'attic'
}
pipeline_map = {
  'input': 0,
  'extraction': 1,
  'evaluation': 2,
  'aggregation': 3,
  'response_evaluation': 4,
  'compression': 5,
  'execution': 6,
  'output_ctrl': 7,
  'output': 8,
  'dm': 9,
  'operations_ctrl': 10
}
ordinal_keys = {
  "A": {
    "id": "",
    "pattern": "^[A|a](bove)",
    'dimension': 'z',
    "value_change": '+1'
  },
  "B": {
    "id": "",
    "pattern": "^[B|b](elow)",
    'dimension': 'z',
    "value_change": '-1'
  },
  "S": {
    "id": "",
    "pattern": "^[S|s](ame|elf)",
    'dimension': 'z',
    "value_change": '0'
  }
}
# cardinal_keys={
#   'N': {
#     'id': '',
#     "pattern": '^[B|b](elow)',
#     'dimension': 'z',
#     'value_change': 0,
#     'operation': 'rotate_reader_head_to'
#   },
#   'E': {
#     'id': '',
#     "pattern": '^[B|b](elow)',
#     'dimension': 'z',
#     'value_change': 90,
#     'operation': 'rotate_reader_head_to'
#   },
#   'S': {
#     'id': '',
#     "pattern": '^[B|b](elow)',
#     'dimension': 'z',
#     'value_change': 180,
#     'operation': 'rotate_reader_head_to'
#   },
#   'W': {
#     'id': '',
#     "pattern": '^[B|b](elow)',
#     'dimension': 'z',
#     'value_change': 270,
#     'operation': 'rotate_reader_head_to'
#   },
# }
floor_order = [
  'cellar',
  'basement',
  'archive',
  'main',
  'attic'
]


class Floors(Enum):
  CELLAR = 1
  BASEMENT = 2
  ARCHIVE = 3
  MAIN = 4
  ATTIC = 5

  def describe(self):
    return 'Matrix section', self.name

# class OrdinalX(Enum):
#   UNSET = 1
# class OrdinalY(Enum):
#   UNSET = 1
# class OrdinalZ(Enum):
#   UNSET = 1
#   BELOW = 100
#   BETWEEN = 200
#   CENTER = 201
#   MIDDLE = 202
#   ABOVE = 300