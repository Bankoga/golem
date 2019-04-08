from components.base.mechanisms.cogs.producer import Producer
from components.axioms.cell_types import CellType, cell_data
from components.enums.prop_types import PackagerType
from components.enums.pos import CtgType
from utils.helpers.prop_gen_help import kin_label_gen_unique
from components.instructions.collector import Collector
from components.vars.data import Address


class Cell(Producer):
  def __init__(self, *args, **kwargs):
    kwargs['ctg'] = CtgType.PACKAGER
    super().__init__(*args, **kwargs)

  @property
  def cell_type(self):
    return self.var[1]
  @cell_type.setter
  def cell_type(self, value):
    raise RuntimeError('Can not set value of cell type')

  @property
  def source_index(self):
    return self.var[2]
  @source_index.setter
  def source_index(self, value):
    raise RuntimeError('Can not set value of source index')
  
  @property
  def source_shape(self):
    return self.var[3]
  @source_shape.setter
  def source_shape(self, value):
    raise RuntimeError('Can not set value of source shape')

  # WHERE ARE THE LOCALIZED_CONV WEIGHTS? inside collectors and their segments
  # WHERE ARE SAID WEIGHTS PLASTICALLY UPDATED?
  # WHERE ARE SAID WEIGHTS USED?
  # WERE ARE SAID WEIGHTS INITIALIZED? inside collectors and their segments

  def read_data(self, cell_type):
    type_data = cell_data[cell_type.name]
    self.collector_defs = type_data['collector_defs']
    self.freq_range = type_data['freq_range']
    self.init_freq = type_data['init_freq']
    self.pct_of_pod = type_data['pct_of_pod']
    self.init_threshhold = type_data['init_threshhold']
    self.activation_function = type_data['activation_function']
  
  def create_collectors_from_def(self, name, collector_def):
    if collector_def is None:
      raise RuntimeError('It is recommended to have an actual collector def when trying to create cells!')
    collectors = []
    segment_defs = collector_def[1]
    resource_accepted=collector_def[2]
    for direction in collector_def[0]:
      child_label = f'{name}_{direction}'
      new_c = Collector(label=child_label)
      new_c.update(self.registry,
                  self.source_index,
                  self.source_shape,
                  direction,
                  len(segment_defs),
                  resource_accepted,
                  segment_defs)
      new_c.address = Address(**self.address._asdict().copy())
      new_c.address._replace(instruction = child_label)
      new_c.build()
      collectors.append(new_c)
    return collectors

  def create_collectors(self):
    collectors = []
    names = kin_label_gen_unique(self.label, len(self.collector_defs))
    for i,collector_def in enumerate(self.collector_defs):
      collectors.append(self.create_collectors_from_def(names[i], collector_def))
    return collectors

  def build_details(self, *args, **kwargs):
    super().build_details(*args, **kwargs)
    self.read_data(self.cell_type)
    self.create_collectors()

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
  #   "collector_defs":[
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