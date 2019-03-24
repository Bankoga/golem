import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array_equal

from components.data.conv_shape import ConvShape as cs
from components.enums.pos import CtgType
from components.enums.prop_types import RsrcType, RuleType
from components.instructions.conv_instruction import ConvInstruction
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from tests.components.instructions.test_instruction import TestInstruction
from tests.strategies.data_strats import valid_resource_array, valid_shape_and_index, valid_resource_data, valid_sz_shape_and_index
from tests.strategies.func_set_strats import (module_input_set,
                                              processed_module_input_set)
from tests.strategies.pos_strats import valid_direction, valid_pos
from tests.strategies.prop_strats import arb_label, rule_type_prop
from utils.helpers.prop_gen_help import roll_name
from utils.pos import Pos


class TestConvInstruction(TestInstruction):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.INSTRUCTION
    self.rule_type= RuleType.CONV
  
  def set_up_var(self):
    self.registry = AddressRegistry(label='global_address_registry_api')
    self.address = Address(golem='a',matrix='l',func_set='b', stage='a',group='a',packager='p',instruction=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    # self.pos = Pos(self.ctg.get_component_type())
    self.conv_shapes = [cs((4,4),label=f'{self.label}_{roll_name()}'),
                        cs((1),label=f'{self.label}_{roll_name()}'),
                        cs((4,4),label=f'{self.label}_{roll_name()}'),
                        cs((9,9),(1,1),label=f'{self.label}_{roll_name()}'),
                        cs((4,2),(1),label=f'{self.label}_{roll_name()}'),
                        cs((12,12),label=f'{self.label}_{roll_name()}')]
    self.source_shape = (256,256)
    self.source_ind = (45,25)
    self.direction = 'A' # TODO: Use correct ENUM
    self.resource = RsrcType.ENERGY
    self.old_data = []
    self.prev_data = []
    self.values = [self.registry,self.direction,self.resource,self.conv_shapes,self.source_ind,self.source_shape,]
    self.var = tuple(self.values)

  def set_up_dynamic_props(self):
    pass

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.set_up_dynamic_props()
    self.comp = ConvInstruction(self.registry,self.direction,self.resource,self.conv_shapes,self.source_ind,self.source_shape,label=self.label)
    self.comp.build(*self.values)

  def test_instruction_details(self):
    self.assertTrue(self.comp.instruction_details())

  # @given(arb_label(), valid_direction(), st.lists(valid_conv_shape()),valid_pos()) # pylint: disable=no-value-for-parameter
  # def test_default(self, label,direction, conv_shapes,pos):
  #       # for efficiency reasons, eventually instructions will need to be built before processing
  #   inst = ConvInstruction(label,direction, conv_shapes, self.source_ind, self.source_shape,pos)
  #   self.assertEqual(inst.get_ctg(), RuleType.CONV)
  #   self.assertIsNone(inst.curr_shape)
  #   self.assertIsNone(inst.curr_bearing)
  #   self.assertIsNone(inst.curr_pos)
  #   self.assertEqual(inst.direction,direction)
  #   self.assertEqual(inst.var,conv_shapes)
  #   self.assertEqual(inst.ind,self.source_ind)
  #   self.assertEqual(inst.shape,self.source_shape)
  #   self.assertEqual(inst.pos,pos)

  @given(valid_resource_array()) # pylint: disable=no-value-for-parameter
  def test_conv(self, npmatrix_array):
    # # TODO: Build a valid package for a specific id strategy
    # """ what needs to be considered when applying a conv to an arbitrary matrix?
    #     these are all part of the conv considerations
    #     The matrix has already been grabbed at this point!
    #     what about size mismatches between regions? We care about those
    #     Where is activity tracked for plasticity? inside the instruction
    # """
    # result = self.comp.conv(npmatrix_array)
    # expectation = 0
    # a convolution is the dot product of two vectors
    # convs here, use source and compression/expansion aware indexing for slice extraction
    # why not just use the index directly, and grab everything from there in ascending order?
    # # extract the slice of the matrix we wish to use for the convolution with empty space fill
    # # self.comp.extract(npmatrix)
    # self.assertEqual(result,expectation)
    pass

  @given(valid_sz_shape_and_index())
  def test_extract_quadrant(self, sz_shape_and_index):
    input_shape, input_ind,side_sz = sz_shape_and_index
    x = input_ind[0]
    if len(input_ind) > 1:
      y = input_ind[1]
      expectation = input_shape[x:x+side_sz][y:y+side_sz]
    else:
      expectation = input_shape[x:x+side_sz]
    res = self.comp.extract_quadrant(input_ind,input_shape,side_sz)
    self.assertTrue(array_equal(res, expectation))

  @given(valid_shape_and_index())
  def test_extract_quadrant_arbitrary_size(self, side_sz,shape_and_index):
    valid_sz = shape_and_index[0] 
    if len(shape_and_index > 1):
      valid_sz = min(shape_and_index[0],shape_and_index[1])
    if 0 <= side_sz and side_sz <= valid_sz:
      self.test_extract_quadrant((shape_and_index[0],shape_and_index[1],side_sz))
    else:
      with self.assertRaises(RuntimeError):
        self.comp.extract_quadrant((shape_and_index[0],shape_and_index[1],side_sz))

  @given(valid_shape_and_index(),valid_resource_data())
  def test_extract_quadrants(self, shape_and_index, input_shape):
    source_shape, source_ind = shape_and_index
    pass
    """
    cases
    if i,j is out of bounds:
      raise error
    elif i,j is in bounds:
      raw or adjusted input shape is smaller than weights (padding or no?)
      input shape can support a full slice of size equal to weights
    """
    pass

  # @given(valid_conv_shape(), valid_resource_data()) # pylint: disable=no-value-for-parameter
  # def test_extract(self,conv_shape,npmatrix):
  #   # if the input matrix is smaller than the output matrix or the conv, what do we do?
  #   # slice the marix using the conv shape
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
  
  # @given(st.lists(valid_conv_shape())) # pylint: disable=no-value-for-parameter
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
