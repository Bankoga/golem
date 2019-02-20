from enum import Enum

class PackTypes(Enum):
  AGGREGATE = 0
  OVERLAY = 9

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