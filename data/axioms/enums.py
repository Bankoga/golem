from enum import Enum, auto


class AutoName(Enum):
  def _generate_next_value_(self,name,start,count,last_values):
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

class DimS(Enum):
  UNSET = 1
class DimX(Enum):
  UNSET = 1
class DimY(Enum):
  UNSET = 1
class DimZ(Enum):
  UNSET = 1
  BELOW = 100
  BETWEEN = 200
  CENTER = 201
  MIDDLE = 202
  ABOVE = 300

class RuleType(Enum):
  UNSET = 1
  CELL = 100
  FW_FUNC = 500

 # Consider turning each distinct set of proc groups into enums
# TODO: turn all relevant pos data into enums

# file_type = {
#   'golem': 'golem',
#   'proc': 'proc',
#   'coder': 'cdr'
# }
# coder_types = ['sensor']
# proc_types = ['coder','cortical','gateway']
# group_types = proc_types.extend(coder_types)
# resource_types = {
#   "ElasticActivation":"proxies glutamate, and is used to increase the chance of activation",
#   "Inhibitor":"proxies gaba, and is used to reduce the %chance of activation",
#   "Reward||PlasticActivation":"proxies dopamine, and is used to increase the chance of activation as well as modulate the weight of changes before/after it",
#   "Activant": "proxies acetylcholine, and is used to control baseline firing % chance",
#   "Catalyst": "proxies serotonin, and is used to indicate a reduction of activation threshold in impacted functions"
# }
# ordinator_types = ['asc','dsc'] # eventually will need a pairing ordinator