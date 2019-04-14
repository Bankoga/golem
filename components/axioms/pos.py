from components.axioms.props import label_pattern

lineage_pattern = '^[a-zA-Z0-9_]{2,64}(-[a-zA-Z0-9_]{2,64}){0,5}$'

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
cardinal_keys = {
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


