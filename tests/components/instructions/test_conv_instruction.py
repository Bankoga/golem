import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.prop_types import RuleType

from tests.components.instructions.test_instruction import TestInstruction
from tests.strategies.prop_strats import rule_type_prop, arbitrary_id
from tests.strategies.data_strats import valid_conv_shape, valid_resource_data
from tests.strategies.func_set_strats import module_input_set,processed_module_input_set
from tests.strategies.pos_strats import valid_direction, valid_pos

from utils.pos import Pos
from components.instructions.conv_instruction import ConvInstruction
from numpy import array_equal
from components.data.conv_shape import ConvShape as cs

class TestConvInstruction(TestInstruction):
  def setUp(self):
    self.valid_c_id = 'TotallyValidId'
    self.valid_c_type = RuleType.CONV
    self.pos = Pos(self.valid_c_type.get_component_type())
    self.conv_shapes = [cs(self.pos,(4,4)),
                   cs(self.pos,(1)),
                   cs(self.pos,(4,4)),
                   cs(self.pos,(9,9),(1,1)),
                   cs(self.pos,(4,2),(1)),
                   cs(self.pos,(12,12))]
    self.source_shape = (256,256)
    self.source_ind = (45,25)
    self.direction = 'A' # TODO: Use correct ENUM
    self.comp = ConvInstruction(self.valid_c_id,self.direction,self.conv_shapes, self.source_ind,self.source_shape,self.pos)

  @given(arbitrary_id(), valid_direction(), st.lists(valid_conv_shape()),valid_pos()) # pylint: disable=no-value-for-parameter
  def test_default(self, itm_id,direction, conv_shapes,pos):
        # for efficiency reasons, eventually instructions will need to be built before processing
    inst = ConvInstruction(itm_id,direction, conv_shapes, self.source_ind, self.source_shape,pos)
    self.assertEqual(inst.get_ctg(), RuleType.CONV)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.direction,direction)
    self.assertEqual(inst.var,conv_shapes)
    self.assertEqual(inst.ind,self.source_ind)
    self.assertEqual(inst.shape,self.source_shape)
    self.assertEqual(inst.pos,pos)

  # @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  # def test_conv(self, npmatrix):
  #   # TODO: Build a valid package for a specific id strategy
  #   """ what needs to be considered when applying a conv to an arbitrary matrix?
  #       these are all part of the conv considerations
  #       The matrix has already been grabbed at this point!
  #       what about size mismatches between regions? We care about those
  #       Where is activity tracked for plasticity? inside the instruction
  #   """
  #   result = self.comp.conv(npmatrix)
  #   expectation = 0
  #   # extract the slice of the matrix we wish to use for the convolution with empty space fill
  #   # self.comp.extract(npmatrix)
  #   self.assertEqual(result,expectation)


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

  def test_post_init_build_status(self):
    self.assertTrue(self.comp.is_built())
  
  def test_build(self):
    self.assertTrue(self.comp.is_built())
  
  @given(st.lists(valid_conv_shape())) # pylint: disable=no-value-for-parameter
  def test_update_data_built(self,new_data):
    with self.assertRaises(RuntimeError):
      self.comp.build()

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_update_data_unbuilt(self,new_data):
    with self.assertRaises(RuntimeError):
      self.comp.update(new_data)

  # @given(processed_module_input_set()) # pylint: disable=no-value-for-parameter
  # def test_(self, inputs):

  # def test_update_weight(self,updates):
  #   """
  #   because plasticity is handled at the parent level of instructions
  #   we need to ensure that each instruction can have it's weights updated properly
  #   """
  #   pass

  
  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def reset(self, new_data):
    with self.assertRaises(RuntimeError):
      self.comp.reset(new_data)

if __name__ == '__main__':
  unittest.main()