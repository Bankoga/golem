import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal

from components.data.collector_segment import CollectorSegment as cs
from components.enums.pos import CtgType
from components.enums.prop_types import RsrcType, RuleType
from components.instructions.collector import Collector
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from tests.components.instructions.test_instruction import TestInstruction
from tests.strategies.data_strats import (valid_resource_array,
                                          valid_resource_data, valid_shape,
                                          valid_shape_and_index,
                                          valid_sz_shape_and_index)
from tests.strategies.instruction_strats import (valid_collector_segment)
from tests.strategies.func_set_strats import (module_input_set,
                                              processed_module_input_set)
from tests.strategies.pos_strats import valid_direction, valid_pos
from tests.strategies.prop_strats import arb_label, rule_type_prop
from utils.helpers.prop_gen_help import roll_name
from utils.pos import Pos
from math import isnan

class TestCollector(TestInstruction):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.INSTRUCTION
    self.rule_type= RuleType.CONV
    self.max_resources = 256
  
  def set_up_var(self):
    self.registry = AddressRegistry(label='global_address_registry_api')
    self.address = Address(golem='a',matrix='l',func_set='b', stage='a',group='a',packager='p',instruction=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.collector_segment_defs = [
      (self.address,(4,4)),
      (self.address,tuple([1])),
      (self.address,(4,4)),
      (self.address,(9,9),(1,1)),
      (self.address,(4,2),tuple([1])),
      (self.address,(12,12))
    ]
    self.source_shape = (256,256)
    self.source_index = (45,25)
    self.step_direction = 'A' # TODO: Use correct ENUM
    self.num_steps = len(self.collector_segment_defs)
    self.resource_accepted = RsrcType.ENERGY
    self.values = [self.registry,
                   self.source_index,
                   self.source_shape,
                   self.step_direction,
                   self.num_steps,
                   self.resource_accepted,
                   self.collector_segment_defs
                  ]
    self.var = tuple(self.values)
    self.attenuation_rate = 2.5

  def set_up_dynamic_props(self):
    # self.pos = Pos(self.ctg.get_component_type())
    self.collector_segments = [cs(address=self.address,source_index=self.source_index,fill_shape=(4,4),label=f'{self.label}_{roll_name()}'),
                        cs(address=self.address,source_index=self.source_index,fill_shape=tuple([1]),label=f'{self.label}_{roll_name()}'),
                        cs(address=self.address,source_index=self.source_index,fill_shape=(4,4),label=f'{self.label}_{roll_name()}'),
                        cs(address=self.address,source_index=self.source_index,fill_shape=(9,9),label=f'{self.label}_{roll_name()}'),
                        cs(address=self.address,source_index=self.source_index,fill_shape=(4,2),label=f'{self.label}_{roll_name()}'),
                        cs(address=self.address,source_index=self.source_index,fill_shape=(12,12),label=f'{self.label}_{roll_name()}')]
    self.old_data = []
    self.prev_data = []

  def quadrant_helper(self, sz_shape_and_index):
    input_shape, input_ind,side_sz = sz_shape_and_index
    x_sz = side_sz
    y_sz = side_sz
    if type(side_sz) is tuple:
      x_sz = side_sz[0]
      y_sz = side_sz[1]
    x = input_ind[0]
    if len(input_ind) > 1:
      y = input_ind[1]
      expectation = input_shape[x:x+x_sz][y:y+y_sz]
    else:
      expectation = input_shape[x:x+side_sz]
    res = self.comp.extract_quadrant(input_ind,input_shape,side_sz)
    self.assertTrue(array_equal(res, expectation))

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.set_up_dynamic_props()
    self.comp = Collector(self.registry,
                                self.source_index,
                                self.source_shape,
                                self.step_direction,
                                self.num_steps,
                                self.resource_accepted,
                                self.collector_segment_defs,
                                label=self.label)
    self.comp.build(*self.values)

  def test_get_attenuation_rate(self):
    self.assertEqual(self.comp.attenuation_rate, self.attenuation_rate)
  def test_set_attenuation_rate(self):
    with self.assertRaises(RuntimeError):
      self.comp.attenuation_rate = self.attenuation_rate

  def test_instruction_details(self):
    self.assertTrue(self.comp.instruction_details())

  def test_get_source_ind(self):
    self.assertEqual(self.comp.source_index, self.source_index)

  def test_set_source_ind(self):
    with self.assertRaises(RuntimeError):
      self.comp.source_index = self.source_index
    
  def test_get_source_shape(self):
    self.assertEqual(self.comp.source_shape, self.source_shape)
  def test_set_source_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.source_shape = self.source_shape
    
  def test_get_step_direction(self):
    self.assertEqual(self.comp.step_direction, self.step_direction)
  def test_set_step_direction(self):
    with self.assertRaises(RuntimeError):
      self.comp.step_direction = self.step_direction
    
  def test_get_resource_accepted(self):
    self.assertEqual(self.comp.resource_accepted, self.resource_accepted)
  def test_set_resource_accepted(self):
    with self.assertRaises(RuntimeError):
      self.comp.resource_accepted = self.resource_accepted
    
  def test_get_collector_segment_defs(self):
    for i,cnv_shp in enumerate(self.comp.collector_segment_defs):
      self.assertEqual(cnv_shp[0], self.collector_segment_defs[i][0])

  def test_set_collector_segment_defs(self):
    with self.assertRaises(RuntimeError):
      self.comp.collector_segment_defs = self.collector_segment_defs

  @given(st.lists(valid_shape())) # pylint: disable=no-value-for-parameter
  def test_set_up_collector_segments(self,collector_segment_defs):
    self.comp.set_up_collector_segments(collector_segment_defs)
    for i,(addr,f_shape) in enumerate(collector_segment_defs):
      self.assertTrue(self.comp.collector_segments[i].address == addr)
      self.assertTrue(self.comp.collector_segments[i].fill_shape == f_shape)

  def test_get_collector_segments(self):
    self.assertEqual(self.comp.collector_segments, self.collector_segments)

  def test_set_collector_segments(self):
    with self.assertRaises(RuntimeError):
      self.comp.collector_segments = self.collector_segments

  @given(st.tuples(st.integers(),st.integers()))
  def test_get_side_szs(self, side_sz):
    x_sz = side_sz
    y_sz = side_sz
    if type(side_sz) is tuple:
      x_sz = side_sz[0]
      y_sz = side_sz[1]
    res_x, res_y = self.comp.get_side_szs(side_sz)
    self.assertEqual(res_x, x_sz)
    self.assertEqual(res_y, y_sz)

  @given(valid_sz_shape_and_index()) # pylint: disable=no-value-for-parameter
  def test_extract_quadrant(self, sz_shape_and_index):
    self.quadrant_helper(sz_shape_and_index)

  @given(valid_collector_segment(),valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_apply_collector_segment(self, coll_sgmnt, resource_data):
    if not self.comp.is_registered:
      self.comp.register(self.address)
    # conv_quad = self.comp.extract_quadrant(self.source_index, resource_data, coll_sgmnt.fill_shape)
    # expectation = array(coll_sgmnt.weights.shape) #this is a numpy array that is the dot product of the two arrays
    # if coll_sgmnt is None:
    #   with self.assertRaises(AttributeError):
    #     res = self.comp.apply_collector_segment(coll_sgmnt, resource_data)
    res = self.comp.apply_collector_segment(coll_sgmnt, resource_data)
    self.assertTrue(res.shape == coll_sgmnt.weights.shape)
    for i in range(len(coll_sgmnt.weights)):
      for j in range(len(coll_sgmnt.weights[i])):
        self.assertTrue(0 <= res[i][j] and not isnan(res[i][j]))

  #   res = self.comp.apply_collector_segment(cnv_shp, resource_data)
  #   self.assertEqual(res, expectation)

  # @given(valid_resource_array()) # pylint: disable=no-value-for-parameter
  # def test_conv(self, npmatrix_array):
  #   # # TODO: Build a valid package for a specific id strategy
  #   # """ what needs to be considered when applying a conv to an arbitrary matrix?
  #   #     these are all part of the conv considerations
  #   #     The matrix has already been grabbed at this point!
  #   #     what about size mismatches between regions? We care about those
  #   #     Where is activity tracked for plasticity? inside the instruction
  #   # """
  #   # result = self.comp.conv(npmatrix_array)
  #   # expectation = 0
  #   # a convolution is the dot product of two vectors
  #   # convs here, use source and compression/expansion aware indexing for slice extraction
  #   # why not just use the index directly, and grab everything from there in ascending order?
  #   # # extract the slice of the matrix we wish to use for the convolution with empty space fill
  #   # # self.comp.extract(npmatrix)
  #   # self.assertEqual(result,expectation)
  #   pass

  # @given(processed_module_input_set()) # pylint: disable=no-value-for-parameter
  # def test_get_input(self,inputs):
  #   pass

  # @given(processed_module_input_set()) # pylint: disable=no-value-for-parameter
  # def test_operate(self, inputs):
  #   """
  #   At a cell level, we execute all of our instructions using a method provided by the context
  #   At an instruction level, we execute on the inputs within context in the direction specified using the contextual cardinator
  #   for each direction
  #     take a sample of the package shape for each shape
  #     record activity information while sampling
  #   combine all samples into a single result using distance attenuation
  #   """
  #   packages = inputs[0]
  #   fs = inputs[1]
  #   result = self.comp.operate(packages,fs)
  #   parts = []
  #   # for pack in inputs:
  #   # for each instruction
  #   #   we grab specifed_input from the inputs
  #   #   we apply a 2d convolution with the specified shape
  #   #   we do what with the result?

  # def test_post_init_build_status(self):
  #   self.assertTrue(self.comp.is_built())
  
  # def test_build(self):
  #   self.assertTrue(self.comp.is_built())
  
  # @given(st.lists(valid_collector_segment())) # pylint: disable=no-value-for-parameter
  # def test_update_data_built(self,new_data):
  #   with self.assertRaises(RuntimeError):
  #     self.comp.build()

  # @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  # def test_update_data_unbuilt(self,new_data):
  #   with self.assertRaises(RuntimeError):
  #     self.comp.update(new_data)

  # @given(processed_module_input_set()) # pylint: disable=no-value-for-parameter
  # def test_(self, inputs):

  # def test_update_weight(self,updates):
  #   """
  #   because plasticity is handled at the parent level of instructions
  #   we need to ensure that each instruction can have it's weights updated properly
  #   """
  #   pass

  
  # @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  # def reset(self, new_data):
  #   with self.assertRaises(RuntimeError):
  #     self.comp.reset(new_data)

if __name__ == '__main__':
  unittest.main()
