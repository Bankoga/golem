import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.axioms.enums import RuleType
from tests.strategies.enum_strats import ruletype
from tests.strategies.packing_strats import valid_directions, valid_shapes

from utils.pos import Pos
from utils.conv_instruction import ConvInstruction

class TestInstruction(unittest.TestCase):
  def setUp(self):
    # self.inst = ConvInstruction(RuleType.CELL)
    pass

  @given(valid_directions(), valid_shapes()) # pylint: disable=no-value-for-parameter
  def test_default(self, directions, shapes):
    inst = ConvInstruction(directions, shapes)
    self.assertEqual(inst.type, RuleType.CELL)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.directions,directions)
    self.assertEqual(inst.shapes,shapes)

  def test_perform(self, package):
    pass

if __name__ == '__main__':
  unittest.main()