from data.axioms.enums import RuleType
from abc import abstractmethod

class PackagingRule:
  """
  The actual functions that power the matrix
  Not the groups, or the meta-containers, or regions, but the functions themselves
  Examples of Packaging Rule Types:
    - Cell Type
    - Framework Function
  We are going to need another metaprovider here.
  """

  def __init__(self, rule_type, arb_id):
    self.type = rule_type
    self.id = arb_id

  @abstractmethod
  def pack(self, inputs):
    pass