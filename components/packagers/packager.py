from abc import abstractmethod
from components.base.mechanisms.producer import Producer

from components.axioms.packager import defaults as prd
from components.enums.prop_types import PackagerType

class Packager(Producer):
  """
  The actual algorithms that power the matrix
  Not the function sets, or the meta-containers, or regions, but a unified algorithm or method
  Examples of Packager Types:
    - Cell
    - Framework Function
  We are going to need another metaprovider here.
  All packagers use multiple instructions to transform input into output
  """

  def __init__(self, rule_type, arb_label):
    super().__init__(arb_label, rule_type.get_component_type(),rule_type)
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