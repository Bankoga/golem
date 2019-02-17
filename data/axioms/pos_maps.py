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
direction_keys = {
  "A": {
    "id": "",
    "pattern": "^[A|a](bove)",
    "position_key": ""
  }
}