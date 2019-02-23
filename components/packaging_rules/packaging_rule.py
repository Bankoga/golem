from data.axioms.enums import RuleType
from data.axioms.configs import packaging_rule_defaults as prd
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
    self.freq_range = prd['freq_range']
    self.init_freq = prd['init_freq']
    self.pct_of_pod = prd['pct_of_pod']
    self.init_threshhold = prd['init_threshhold']
    self.activation_function = prd['activation_function']

  @abstractmethod
  def pack(self, inputs):
    pass