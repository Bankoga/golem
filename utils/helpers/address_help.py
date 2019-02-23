
def build_address(module_id, group_id):
  if group_id is None:
    return f'{module_id}'
  else:
    return f'{module_id}-{group_id}'

def build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape):
  addr = build_address(rm_id,rg_id)
  if dp_shape is None:
    return f'{addr};{dp_resource};{dp_type}'
  else:
    return f'{addr};{dp_resource};{dp_type};{dp_shape}'