import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.cogs.cells.cell import Cell
from components.enums.pos import CtgType
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from components.axioms.cell_types import CellType, cell_data
from components.enums.prop_types import RuleType, RsrcType, ChannelType,FieldType, PackagerType

from tests.strategies.channel_strats import valid_cell_instruction
from tests.strategies.prop_strats import arb_cell_type, arb_label
from tests.strategies.instruction_strats import arb_full_collector_def
from tests.components.base.mechanisms.cogs.test_producer import TestProducer
from tests.strategies.data_strats import valid_shape

from components.channels.misc_funcs import build_address, build_meld, build_package

class TestCell(TestProducer):
  def set_up_base(self):
    self.label = 'star_0'
    self.ctg = CtgType.PACKAGER
    self.comp_class = Cell

  def set_up_var(self):
    self.registry = AddressRegistry(label='global_registry')
    self.address = Address(golem='a',matrix='l',func_set='b',stage='base',group='randos',packager='star_0')
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.cell_type = CellType.PYRAMID
    self.source_index = (0,0)
    self.source_shape = (256,256)
    self.values = [self.registry,self.cell_type,self.source_index,self.source_shape]
    self.var = tuple(self.values)

  # def set_up_defaults(self):

  def setUp(self):
    self.set_up_base()
    # self.set_up_defaults()
    self.set_up_var()
    self.comp = self.comp_class(label=self.label, ctg=self.ctg)
    self.comp.update(*self.values)

  def test_get_cell_type(self):
    self.assertEqual(self.comp.cell_type, self.cell_type)
  @given(arb_cell_type()) # pylint: disable=no-value-for-parameter
  def test_set_cell_type(self, cell_type):
    with self.assertRaises(RuntimeError):
      self.comp.cell_type = cell_type

  def test_get_source_index(self):
    self.assertEqual(self.comp.source_index, self.source_index)
  @given(valid_shape()) # pylint: disable=no-value-for-parameter
  def test_set_source_index(self, source_index):
    with self.assertRaises(RuntimeError):
      self.comp.source_index = source_index

  def test_get_source_shape(self):
    self.assertEqual(self.comp.source_shape, self.source_shape)
  @given(valid_shape()) # pylint: disable=no-value-for-parameter
  def test_set_source_shape(self, source_shape):
    with self.assertRaises(RuntimeError):
      self.comp.source_shape = source_shape

  def read_data_assertions(self, cell_type):
    expected_data = cell_data[cell_type.name]
    # This doesn't test any of the expectations of the values for those though
    self.assertEqual(self.comp.collector_defs, expected_data['collector_defs'])
    self.assertEqual(self.comp.freq_range, expected_data['freq_range'])
    self.assertEqual(self.comp.init_freq, expected_data['init_freq'])
    self.assertEqual(self.comp.pct_of_pod, expected_data['pct_of_pod'])
    self.assertEqual(self.comp.init_threshhold, expected_data['init_threshhold'])
    self.assertEqual(self.comp.activation_function, expected_data['activation_function'])

  @given(arb_cell_type()) # pylint: disable=no-value-for-parameter
  def test_cell_type_data(self, cell_type):
    if cell_type is None:
      with self.assertRaises(RuntimeError):
        self.comp.read_data(cell_type)
    else:
      self.comp.read_data(cell_type)
      self.read_data_assertions(cell_type)

  def test_determine_residence(self):
    # can proxy for later! wait until post config to post proxy residence buildable golems
    pass

  @given(arb_label(), arb_full_collector_def()) # pylint: disable=no-value-for-parameter
  def test_create_collectors_from_def(self, name, collector_def):
    # Collector defs do what?
    # specify a set of directions to set up collectors
    # each step is represented by a list of filter shapes
    self.comp.address = self.address
    if collector_def is None:
      with self.assertRaises(RuntimeError):
        res = self.comp.create_collectors_from_def(name, collector_def)
    res = self.comp.create_collectors_from_def(name, collector_def)
    for i,item in enumerate(collector_def):
      for ic,c in enumerate(item):
        collector = res[i+ic]
        self.assertEqual(collector.label, f'{name}_{c}')
        self.assertEqual(collector.step_direction, c)
      self.assertEqual(collector.num_steps, len(collector_def[1]))
      self.assertEqual(len(collector.segments), len(collector_def[1]))
      self.assertEqual(collector.resource_accepted, collector_def[2])
      self.assertEqual(collector.source_index, self.source_index)
      self.assertEqual(collector.source_shape, self.source_shape)
    self.assertEqual(self.comp.address, self.address)

  def test_build_with_data(self):
    self.comp = self.comp_class(label=self.label, ctg=self.ctg)
    #  building a cell includes reading the data of any new cell type provided if provided self.read_data()
    #  building requires that a cell have a type != UNSET
    self.comp.build(*self.values, address=self.address)
    self.assertEqual(self.comp.var, self.var)
    self.assertTrue(self.comp.is_built)
    self.read_data_assertions(self.cell_type)

  def test_collect_resources(self):
    # can proxy envs init/connection, and resource existance, but not actual collection
    pass

  # @given()
  # def test_pack(self,inputs):
  #   """
  #  packing may be done in func sets
  #   but I need a guaranteed order to some of the inputs don't I?
  #   Why? Bc agg type packages get combined in a spatially oriented way
  #   Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
  #   Given that each sender has a position, this can be added to the package along with sender address (or in place of?)
  #   Given that we are sent inputs
  #   When we prepare to evaluate them
  #   Then we sort them using a guaranteed sort by pos first!

  #   Where does this sort live? In utils.helpers.pos_help?

  #   Specifiying inputs for testing packages, and things that rely on them is growing more complex
  #   At this point, I think it makes the most sense to begin work on a package series of custom hypothesis strategies

  #   aggregate packages can't exist or not exist as they please
  #   they must always exist in the correct order to be processed
  #   Thus we assume that an order id list or dict has been generated which we can compare against
  #   """
  #   # build a
  #   st.lists(st.builds(build_package, st.sampled_from(['SenderModuleId','self','Self']),
  #       st.sampled_from(['sender_set_id','self','Self', '']),
  #       st.sampled_from(RsrcType),
  #       st.sampled_from(ChannelType),
  #       st.sampled_from(FieldType),
  #       st.sampled_from(['SenderModuleId','self','Self']),
  #       st.sampled_from(['sender_set_id','self','Self',''])))
  #   pass


  # """
  # What happens before a localized conv
  #  patch = we extract a part of the shape
  #   - How do we select which part of the shape to process?
  # """
  # @given(st.text())
  # def test_localized_conv(self, patch):
  #   """
  #   What happens during a localized convolution?
  #   - active_connect = get_random_fill_from(base_weights,mod_weights, other_mods) which incorps the * can_be_active_now
  #   - acutal_inputs = patch * active_connect
  #       the patch is where we can leverage resources from
  #       each resource index, has an independent % chance of being activated though
  #       thus, we must calc the inputs to be used this timestep before doing anything
  #   - 
  #   total_compute_per_simulated_ts = avg_latency_per_simulated_ts + avg_compute_per_simulated_ts
  #   simulated_fps = num_ts_per_simulated_sec + total_compute_per_simulated_ts
  #   there is going to be a slew of timestep logic that spans many components
  #   Not sure as to what needs to be abstracted though
  #   """
  #   pass
  
  # @given(st.text(),st.text())
  # def test_get_activity_data(self, inputs, timestep):
  #   """
  #   each nearby cell, has a % chance of raising the current cells activation probability
  #   chance = Input_Strength - Distance_factor
  #   """
  #   pass

  # @given(st.text())
  # def test_process(self, inputs):
  #   """
  #   given the properties
  #     - collectors
  #     - module_inputs_dict
  #     - module_outputs_dict
  #   when it is time to process inputs
  #   then each instruction should be executed
  #   """
  #   pass
  # # def test_get_random_fill_from(self):
  
  # @given(valid_cell_instruction()) # pylint: disable=no-value-for-parameter
  # def test_exec_instruction(self, instruction):
  #   # directions = instruction[0]
  #   # leaves = instruction[1]
    
  #   pass

if __name__ == '__main__':
  unittest.main()