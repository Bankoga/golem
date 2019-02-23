from data.axioms.enums import RuleType

class PackagingRule:
  """
  The actual functions that power the matrix
  Not the groups, or the meta-containers, or regions, but the functions themselves
  Examples of Packaging Rule Types:
    - Cell Type
    - Framework Function
  We are going to need another metaprovider here.
  """

  def __init__(self, rule_type):
    self.type = rule_type

  def pack(self, inputs):
    pass