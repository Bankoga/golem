import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.axioms.enums import RuleType
from tests.strategies.enum_strats import ruletype
from tests.strategies.packing_strats import valid_shapes
from tests.strategies.pos_strats import valid_directions, valid_pos

from utils.pos import Pos
from utils.conv_instruction import ConvInstruction

class TestConvInstruction(unittest.TestCase):
  def setUp(self):
    # self.inst = ConvInstruction(RuleType.CELL)
    pass

  @given(valid_directions(), valid_shapes(),valid_pos()) # pylint: disable=no-value-for-parameter
  def test_default(self, directions, shapes, pos):
        # for efficiency reasons, eventually instructions will need to be built before processing
    inst = ConvInstruction(directions, shapes, pos)
    self.assertEqual(inst.type, RuleType.CELL)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.directions,directions)
    self.assertEqual(inst.shapes,shapes)
    self.assertEqual(inst.pos,pos)

  def test_perform(self, package):
    """
    for each direction
      take a sample of the package for each shape
      record activity information while sampling
    combine all samples into a single result using distance attenuation
    """

if __name__ == '__main__':
  unittest.main()