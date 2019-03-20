from components.channels.channel import Channel

def build_address(module_id, set_id):
  if set_id is None:
    return f'{module_id}'
  else:
    return f'{module_id}-{set_id}'

def build_meld(ch_type,dp_resource,recip_addr,dp_shape=None):
  if dp_shape is None:
    return f'{ch_type};{dp_resource};{recip_addr}'
  else:
    return f'{ch_type};{dp_resource};{recip_addr};{dp_shape}'

def build_channel_inputs(ch_type,dp_resource,recip_addr,dp_shape, sm_id, sg_id):
  sender_address = build_address(sm_id,sg_id)
  meld = build_meld(ch_type,dp_resource,recip_addr,dp_shape)
  return tuple([meld,sender_address])

def build_package(ch_type,dp_resource,recip_addr,dp_shape, sm_id, sg_id):
  sender_address = build_address(sm_id,sg_id)
  meld = build_meld(ch_type,dp_resource,recip_addr,dp_shape)
  return Channel(meld,sender_address)

def sort_data_packs(self, packages):
  """
  given a list of packages
    sorts into N=ChannelType lists
    said list use a guaranteed insertion sort using sender pos
  """
  pass