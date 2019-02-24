from utils.datapack import Datapack

def build_address(module_id, group_id):
  if group_id is None:
    return f'{module_id}'
  else:
    return f'{module_id}-{group_id}'

def build_meld(recip_addr,dp_resource,dp_type,dp_shape=None):
  if dp_shape is None:
    return f'{recip_addr};{dp_resource};{dp_type}'
  else:
    return f'{recip_addr};{dp_resource};{dp_type};{dp_shape}'

def build_datapack_inputs(recip_addr,dp_resource,dp_type,dp_shape, sm_id, sg_id):
  sender_address = build_address(sm_id,sg_id)
  meld = build_meld(recip_addr,dp_resource,dp_type,dp_shape)
  return tuple([meld,sender_address])

def build_datapack(recip_addr,dp_resource,dp_type,dp_shape, sm_id, sg_id):
  sender_address = build_address(sm_id,sg_id)
  meld = build_meld(recip_addr,dp_resource,dp_type,dp_shape)
  return Datapack(meld,sender_address)

def sort_data_packs(self, datapacks):
  """
  given a list of datapacks
    sorts into N=PackType lists
    said list use a guaranteed insertion sort using sender pos
  """
  pass