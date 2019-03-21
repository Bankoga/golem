# configs axioms are global configuration items
# config axioms are not specific to config files
dirs = {
  'golem': 'configs\\types\\',
  'proc': 'configs\\procs\\',
  'cdr': 'configs\\coders\\',
  'hks': 'configs\\hook_sets\\'
}
file_type = {
  'golem': 'golem',
  'proc': 'proc',
  'coder': 'cdr',
  'hook_set': 'hks'
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
set_ids = proc_ids.copy()
set_ids.update(coder_ids)
resource_types = {
  "ElasticActivation":"proxies glutamate, and is used to increase the chance of activation",
  "Inhibitor":"proxies gaba, and is used to reduce the %chance of activation",
  "Reward||PlasticActivation":"proxies dopamine, and is used to increase the chance of activation as well as modulate the weight of changes before/after it",
  "Activant": "proxies acetylcholine, and is used to control baseline firing % chance",
  "Catalyst": "proxies serotonin, and is used to indicate a reduction of activation threshold in impacted functions"
}