from components.vars.misc import reg_keys, lineage_keys, channel_keys

from numpy import array_equal

def reg_item_check(reg_item):
  item_keys = tuple(reg_item.keys())
  v = array_equal(item_keys, reg_keys)
  return v

def lineage_item_check(lineage_item):
  item_keys = tuple(lineage_item.keys())
  v = array_equal(item_keys, lineage_keys)
  return v

def channel_item_check(channel_item):
  item_keys = tuple(channel_item.keys())
  v = array_equal(item_keys, channel_keys)
  return v