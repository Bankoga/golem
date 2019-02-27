import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.axioms.enums import RuleType
from tests.strategies.enum_strats import ruletype
from tests.strategies.packing_strats import valid_shapes
from tests.strategies.golem_strats import module_input_set
from tests.strategies.pos_strats import valid_direction, valid_pos

from utils.pos import Pos
from components.instructions.conv_instruction import ConvInstruction
from numpy import ones, array_equal

class TestConvInstruction(unittest.TestCase):
  def setUp(self):
    self.inst = ConvInstruction([], [], Pos())

  @given(valid_direction(), valid_shapes(),valid_pos()) # pylint: disable=no-value-for-parameter
  def test_default(self, direction, shapes, pos):
        # for efficiency reasons, eventually instructions will need to be built before processing
    inst = ConvInstruction(direction, shapes, pos)
    self.assertEqual(inst.type, RuleType.CELL)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.direction,direction)
    self.assertEqual(inst.shapes,shapes)
    self.assertEqual(inst.pos,pos)
  
  @given(st.lists(valid_shapes())) # pylint: disable=no-value-for-parameter
  def test_set_up_weights(self,shapes):
    weights = self.inst.set_up_weights(shapes)
    for shape in shapes:
      expectation = ones(shape)
      result = weights[shape]
      self.assertEqual(result.shape, shape)
      self.assertTrue(array_equal(result, expectation))

  @given(module_input_set()) # pylint: disable=no-value-for-parameter
  def test_perform(self, inputs):
    """
    At a cell level, we execute all of our instructions using a method provided by the context
    At an instruction level, we execute on the inputs within context in the direction specified using the contextual cardinator
    for each direction
      take a sample of the package shape for each shape
      record activity information while sampling
    combine all samples into a single result using distance attenuation
    """
    pass

  # def test_update_weight(self,updates):
  #   """
  #   because plasticity is handled at the parent level of instructions
  #   we need to ensure that each instruction can have it's weights updated properly
  #   """
  #   pass

if __name__ == '__main__':
  unittest.main()