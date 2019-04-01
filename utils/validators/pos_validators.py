import re

from components.axioms.pos import address_pattern
from components.enums.pos import CtgType

def is_valid_ctg(ctg):
  return ctg in CtgType

def is_valid_addr(addr):
  res = re.search(address_pattern, addr)
  if res is None:
    return False
  else:
    return len(res.groups()) == 1