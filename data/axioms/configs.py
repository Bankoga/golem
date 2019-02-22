# configs axioms are global configuration items
# config axioms are not specific to config files
dirs = {
  'golem': 'configs\\types\\',
  'proc': 'configs\\procs\\',
  'cdr': 'configs\\coders\\'
}
file_type = {
  'golem': 'golem',
  'proc': 'proc',
  'coder': 'cdr'
}
links = [
  'dm',
  'gate_i',
  'loop_i',
  'synch_i',
  'synch_all'
]
proc_ids = {
  'dcgc': 'DCGC',
  'glg': 'GLG',
  'dcagc': 'DCAGC',
  'dfagc': 'DFAGC',
  'dfgc': 'DFGC'
}
coder_ids = {
  'ps': 'PS'
}
# 'ticg': 'TICG'
# 'aslg': 'ASLG',
# 'slg': 'SLG',
# 'mlg': 'MLG',
# 'kblg': 'KBLG'
procs = proc_ids.values()#['DCLEG','DFLEG','GLG','PICG','POCG','TICG','ASLG','SLG','MLG','KBLG']
coder_types = ['sensor']
proc_types = ['coder','cortical','gateway']
group_types = proc_types.extend(coder_types)
resource_types = {
  "ElasticActivation":"proxies glutamate, and is used to increase the chance of activation",
  "Inhibitor":"proxies gaba, and is used to reduce the %chance of activation",
  "Reward||PlasticActivation":"proxies dopamine, and is used to increase the chance of activation as well as modulate the weight of changes before/after it",
  "Activant": "proxies acetylcholine, and is used to control baseline firing % chance",
  "Catalyst": "proxies serotonin, and is used to indicate a reduction of activation threshold in impacted functions"
}
id_pattern = "[a-zA-Z0-9_]*$"
dest_key_pattern = "[a-zA-Z0-9_].*(-[a-zA-Z0-9_].*)?"
ordinators = ['asc','dsc'] # eventually will need a pairing ordinator