dirs = {
  'golem': 'configs\\types\\',
  'proc': 'configs\\procs\\'
}
file_type = {
  'golem': 'golem',
  'proc': 'proc'
}
links = [
  'dm',
  'gate_i',
  'loop_i',
  'synch_i',
  'synch_all'
]
proc_types = ['coder','cortical','gateway']
proc_ids = {
  'dcgc': 'DCGC',
  'glg': 'GLG',
}
  # 'dcagc': 'DCAGC',
  # 'dfagc': 'DFAGC',
  # 'dfgc': 'DFGC',
  # 'picg': 'PICG',
  # 'pocg': 'POCG'
# 'ticg': 'TICG'
# 'aslg': 'ASLG',
# 'slg': 'SLG',
# 'mlg': 'MLG',
# 'kblg': 'KBLG'
procs = proc_ids.values()#['DCLEG','DFLEG','GLG','PICG','POCG','TICG','ASLG','SLG','MLG','KBLG']
# I do not know why I wrote this groups object. The intent eludes me
groups = {
  '': {}
}
