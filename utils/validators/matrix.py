from components.vars.misc import reg_keys, addr_keys

from numpy import array_equal

def reg_item_check(reg_item):
  item_keys = list(reg_item.keys())
  v = array_equal(item_keys, reg_keys)
  return v

def addr_item_check(addr_item):
  item_keys = list(addr_item.keys())
  v = array_equal(item_keys, addr_keys)
  return v