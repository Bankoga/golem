import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.enums.prop_types import RuleType

from tests.components.instructions.test_instruction import TestInstruction
from tests.strategies.prop_strats import rule_type_prop, arbitrary_id
from tests.strategies.packing_strats import valid_conv_shape,valid_resource_data
from tests.strategies.func_set_strats import module_input_set,processed_module_input_set
from tests.strategies.pos_strats import valid_direction, valid_pos

from utils.pos import Pos
from components.instructions.conv_instruction import ConvInstruction
from numpy import array_equal
from utils.conv_shape import ConvShape as cs

class TestConvInstruction(TestInstruction):
  def setUp(self):
    self.valid_c_id = 'TotallyValidId'
    self.valid_c_type = RuleType.CONV
    self.conv_shapes = [cs((4,4)),
                   cs((1)),
                   cs((4,4)),
                   cs((9,9),(1,1)),
                   cs((4,2),(1)),
                   cs((12,12))]
    self.source_shape = (256,256)
    self.source_ind = (45,25)
    self.direction = 'A' # TODO: Use correct ENUM
    self.pos = Pos()
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

  @given(processed_module_input_set()) # pylint: disable=no-value-for-parameter
  def test_operate(self, inputs):
    """
    At a cell level, we execute all of our instructions using a method provided by the context
    At an instruction level, we execute on the inputs within context in the direction specified using the contextual cardinator
    for each direction
      take a sample of the package shape for each shape
      record activity information while sampling
    combine all samples into a single result using distance attenuation
    """
    packages = inputs[0]
    fs = inputs[1]
    result = self.comp.operate(packages,fs)
    parts = []
    # for pack in inputs:
    # for each instruction
    #   we grab specifed_input from the inputs
    #   we apply a 2d convolution with the specified shape
    #   we do what with the result?

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_conv(self, npmatrix):
    # TODO: Build a valid package for a specific id strategy
    """ what needs to be considered when applying a conv to an arbitrary matrix?
        these are all part of the conv considerations
        what about size mismatches between regions?
        which index do we center on? the source index
        Where do the weights reside? 
        How is activity tracked for plasticity?
    """
    result = self.comp.conv(npmatrix)
    expectation = 0
    self.assertEqual(result,expectation)

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