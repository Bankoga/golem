from components.axioms.props import id_pattern
import re

def is_valid_label(label):
  if len(re.findall(id_pattern, label)) == 1:
    return True
  else:
    return False