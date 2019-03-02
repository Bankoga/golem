from abc import abstractmethod
from components.component import Component

from data.axioms.packager import defaults as prd
from data.enums.prop_types import NodeType

class Packager(Component):
  """
  The actual functions that power the matrix
  Not the groups, or the meta-containers, or regions, but the functions themselves
  Examples of Packaging Rule Types:
    - Cell Type
    - Framework Function
  We are going to need another metaprovider here.
  """

  def __init__(self, rule_type, arb_id):
    super().__init__(arb_id, rule_type.get_component_type(),rule_type)
    self.read_data()

  @abstractmethod
  def pack(self, inputs):
    pass

  @abstractmethod
  def read_data(self):
    self.freq_range = prd['freq_range']
    self.init_freq = prd['init_freq']
    self.pct_of_pod = prd['pct_of_pod']
    self.init_threshhold = prd['init_threshhold']
    self.activation_function = prd['activation_function']