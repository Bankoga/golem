from components.base.mechanisms.cogs.producer import Producer
from components.axioms.cell_types import CellType, cell_data
from components.enums.prop_types import PackagerType
from components.enums.pos import CtgType

class Cell(Producer):
  # def __init__(self, rule_type, arb_label):
  #   super().__init__(arb_label, rule_type.get_component_type(),rule_type)
  
  def __init__(self, *args, **kwargs):
    cell_type = CellType.UNSET
    if len(args) > 0:
      cell_type = args[0]
      args = [].extend(args)
    kwargs['ctg'] = CtgType.PACKAGER
    super().__init__(*args, **kwargs)
    self.read_data(cell_type)

  # WHERE ARE THE LOCALIZED_CONV WEIGHTS? inside collectors and their segments
  # WHERE ARE SAID WEIGHTS PLASTICALLY UPDATED?
  # WHERE ARE SAID WEIGHTS USED?
  # WERE ARE SAID WEIGHTS INITIALIZED? inside collectors and their segments

  def read_data(self, cell_type):
    type_data = cell_data[cell_type.name]
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