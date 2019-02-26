from components.packaging_rules import packaging_rule
from data.axioms.cell_types import CellType, cell_data
from data.axioms.enums import RuleType

class Cell(packaging_rule.PackagingRule):
  
  def __init__(self, cell_id):
    if (not cell_id in CellType) or cell_id == CellType.UNSET:
      super().__init__(RuleType.CELL, CellType.PYRAMID)
    else:
      super().__init__(RuleType.CELL, cell_id)
    # self.setup_convs()
    # self.?
  
  # WHERE ARE THE LOCALIZED_CONV WEIGHTS?
  # WHERE ARE SAID WEIGHTS PLASTICALLY UPDATED?
  # WHERE ARE SAID WEIGHTS USED?
  # WERE ARE SAID WEIGHTS INITIALIZED?

  def read_data(self):
    s = str(self.id)
    type_data = cell_data[s]
    self.cnv_tmplts = type_data['cnv_tmplts']
    self.freq_range = type_data['freq_range']
    self.init_freq = type_data['init_freq']
    self.pct_of_pod = type_data['pct_of_pod']
    self.init_threshhold = type_data['init_threshhold']
    self.activation_function = type_data['activation_function']
  
  def pack(self,inputs):
    pass
  
  def localized_conv(self, shape):
    pass
  
  def process(self):
    pass
  """
  A function group consists of multiple cells
  A cell consists of multiple convolutions with potentially different types of inputs
  """

  def exec_instruction(self, instruction):
    pass

  # TODO: Define where CellType resource data is stored in the configs, and in object creation

  # 'CellType.PYRAMID': {
  #   "cnv_tmplts":[
  #     ["A",["1x1","1x1","1x1","4x4","8x8"]],
  #     ["B",["4x4"]],
  #     ["B",["8x8,1"]],
  #     ["S",["3x3"]]
  #   ],
  #   "freq_range": [5,256],
  #   "init_freq": 5,
  #   "pct_of_pod": 0,
  #   "init_threshhold":0.98,
  #   "activation_function":"tanh"
  # },