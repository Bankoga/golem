from components.axioms.props import id_pattern
import re

def is_valid_id(itm_id):
  if len(re.findall(id_pattern, itm_id)) == 1:
    return True
  else:
    return False