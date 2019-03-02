from data.axioms.configs import coder_ids, proc_ids, group_ids
from data.enums.prop_types import GroupType

def get_ids(group_type):
  if group_type is None or group_type is GroupType.UNSET:
    raise ValueError('Supplied Invalid Group Type')
  else:
    if 100 < group_type.value and group_type.value < 200:
      result = list(coder_ids.values())
    elif 200 < group_type.value and group_type.value < 300:
      result = list(proc_ids.values())
    else:
      result = []
    return result