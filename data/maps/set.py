from data.axioms.configs import coder_ids, proc_ids, set_ids
from data.enums.prop_types import SetType

def get_ids(set_type):
  if set_type is None or set_type is SetType.UNSET:
    raise ValueError('Supplied Invalid Set Type')
  else:
    if 100 < set_type.value and set_type.value < 200:
      result = list(coder_ids.values())
    elif 200 < set_type.value and set_type.value < 300:
      result = list(proc_ids.values())
    else:
      result = []
    return result