from components.packaging_rules import packaging_rule
from data.axioms.enums import RuleType

class Cell(packaging_rule.PackagingRule):
  
  def __init__(self):
    super().__init__(RuleType.CELL)