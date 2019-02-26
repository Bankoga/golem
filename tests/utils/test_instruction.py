import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.axioms.enums import RuleType
from tests.strategies.enum_strats import ruletype

from utils.pos import Pos
from utils.instruction import Instruction

class TestInstruction(unittest.TestCase):
  def setUp(self):
    self.instruction = Instruction(RuleType.CELL)

  @given(ruletype()) # pylint: disable=no-value-for-parameter
  def test_default(self, rtype):
    inst = Instruction(rtype)
    self.assertEqual(inst.type, rtype)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)

  def test_perform(self, package):
    pass

if __name__ == '__main__':
  unittest.main()