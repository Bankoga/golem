import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.enums.prop_types import RuleType

from tests.components.instructions.test_instruction import TestInstruction
from tests.strategies.prop_strats import rule_type_prop, arbitrary_id
from tests.strategies.packing_strats import valid_shape,valid_resource_data
from tests.strategies.func_set_strats import module_input_set,processed_module_input_set
from tests.strategies.pos_strats import valid_direction, valid_pos

from utils.pos import Pos
from components.instructions.conv_instruction import ConvInstruction
from numpy import ones, array_equal

class TestConvInstruction(TestInstruction):
  def setUp(self):
    self.valid_c_id = 'TotallyValidId'
    self.valid_c_type = RuleType.CONV
    self.shapes = []
    self.direction = ''
    self.pos = Pos()
    self.comp = ConvInstruction(self.valid_c_id,self.direction,self.shapes, self.pos)

  @given(arbitrary_id(), valid_direction(), valid_shape(),valid_pos()) # pylint: disable=no-value-for-parameter
  def test_default(self, itm_id,direction, shapes, pos):
        # for efficiency reasons, eventually instructions will need to be built before processing
    inst = ConvInstruction(itm_id,direction, shapes, pos)
    self.assertEqual(inst.get_ctg(), RuleType.CONV)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.direction,direction)
    self.assertEqual(inst.shapes,shapes)
    self.assertEqual(inst.pos,pos)
  
  @given(st.lists(valid_shape())) # pylint: disable=no-value-for-parameter
  def test_set_up_weights(self,shapes):
    weights = self.comp.set_up_weights(shapes)
    for shape in shapes:
      expectation = ones(shape)
      result = weights[shape]
      self.assertEqual(result.shape, shape)
      self.assertTrue(array_equal(result, expectation))

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
    self.comp.build()
    result = self.comp.operate(packages,fs)
    parts = []
    # for pack in inputs:
    # for each instruction
    #   we grab specifed_input from the inputs
    #   we apply a 2d convolution with the specified shape
    #   we do what with the result?

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_conv(self, matrix):
    """ what needs to be considered when applying a conv to an arbitrary matrix?
        these are all part of the conv considerations
        what about size mismatches between regions?
        which index do we center on?
        Where do the weights reside?
        How is activity tracked for plasticity?
    """

  def test_build(self):
    comp = ConvInstruction(self.valid_c_id, [],[],self.pos)
    self.assertFalse(comp.is_built())
    comp.build()
    self.assertTrue(comp.is_built())
    expected_weights = self.comp.set_up_weights(self.comp.shapes)
    result_weights = comp.var
    self.assertTrue(array_equal(result_weights,expected_weights))
    comp.operate()
  
  # @given(processed_module_input_set()) # pylint: disable=no-value-for-parameter
  # def test_(self, inputs):

  # def test_update_weight(self,updates):
  #   """
  #   because plasticity is handled at the parent level of instructions
  #   we need to ensure that each instruction can have it's weights updated properly
  #   """
  #   pass

if __name__ == '__main__':
  unittest.main()