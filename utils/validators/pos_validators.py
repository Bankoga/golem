import re

from components.axioms.pos import lineage_pattern
from components.enums.pos import CtgType

def is_valid_ctg(ctg):
  return ctg in CtgType

def is_valid_lineage(lineage):
  res = re.search(lineage_pattern, lineage)
  if res is None:
    return False
  else:
    return len(res.groups()) == 1