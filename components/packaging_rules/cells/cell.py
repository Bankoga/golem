from components.packaging_rules import packaging_rule
from data.axioms.cell_types import CellType, cell_data
from data.axioms.enums import RuleType

class Cell(packaging_rule.PackagingRule):
  
  def __init__(self, cell_id):
    if (not cell_id in CellType) or cell_id == CellType.UNSET:
      super().__init__(RuleType.CELL, CellType.PYRAMID)
    else:
      super().__init__(RuleType.CELL, cell_id)
  
  def read_data(self):
    s = str(self.id)
    type_data = cell_data[s]
    self.cnv_tmplts = type_data['cnv_tmplts']
    self.freq_range = type_data['freq_range']
    self.init_freq = type_data['init_freq']
    self.pct_of_pod = type_data['pct_of_pod']
    self.init_threshhold = type_data['init_threshhold']
    self.activation_function = type_data['activation_function']
    