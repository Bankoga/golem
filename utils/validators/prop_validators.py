from components.axioms.props import label_pattern
import re

def is_valid_label(label):
  if len(re.findall(label_pattern, label)) == 1:
    return True
  else:
    return False