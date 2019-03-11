from components.axioms.configs import coder_ids, proc_ids, set_ids
from components.enums.prop_types import SuperSet

def get_ids(set_type):
  if set_type is None or set_type is SuperSet.UNSET:
    raise ValueError('Supplied Invalid Set Type')
  else:
    if set_type is SuperSet.CODER:# if 100 < set_type.value and set_type.value < 200:
      result = list(coder_ids.values())
    elif set_type is SuperSet.PROC:#elif 200 < set_type.value and set_type.value < 300:
      result = list(proc_ids.values())
    else:
      result = []
    return result