from components.base.mechanisms.cogs.producer import Producer
from components.axioms.cell_types import CellType, cell_data
from components.enums.prop_types import PackagerType

class Cell(Producer):
  
  """
  The actual algorithms that power the matrix
  Not the function sets, or the meta-containers, or regions, but a unified algorithm or method
  Examples of producer Types:
    - Cell
    - Framework Function
  We are going to need another metaprovider here.
  All packagers use multiple instructions to transform input into output
  """
  # def __init__(self, rule_type, arb_label):
  #   super().__init__(arb_label, rule_type.get_component_type(),rule_type)
  #   self.read_data()
  # @abstractmethod
  # def pack(self, inputs):
  #   pass
  # @abstractmethod
  # def read_data(self):
  #   self.freq_range = prd['freq_range']
  #   self.init_freq = prd['init_freq']
  #   self.pct_of_pod = prd['pct_of_pod']
  #   self.init_threshhold = prd['init_threshhold']
  #   self.activation_function = prd['activation_function']
  def __init__(self, cell_id):
    if (not cell_id in CellType) or cell_id == CellType.UNSET:
      super().__init__(PackagerType.CELL, CellType.PYRAMID)
    else:
      super().__init__(PackagerType.CELL, cell_id)
    # self.setup_convs()
    # self.?
  
  # WHERE ARE THE LOCALIZED_CONV WEIGHTS? inside collectors and their segments
  # WHERE ARE SAID WEIGHTS PLASTICALLY UPDATED?
  # WHERE ARE SAID WEIGHTS USED?
  # WERE ARE SAID WEIGHTS INITIALIZED? inside collectors and their segments

  def read_data(self):
    s = str(self.get_id())
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