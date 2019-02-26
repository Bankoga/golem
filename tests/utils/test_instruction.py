import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.axioms.enums import RuleType
from tests.strategies.enum_strats import ruletype
from tests.strategies.pos_strats import valid_pos

from utils.pos import Pos
from utils.instruction import Instruction

class TestInstruction(unittest.TestCase):
  def setUp(self):
    # self.instruction = Instruction(RuleType.CELL, )
    pass

  @given(ruletype(), valid_pos()) # pylint: disable=no-value-for-parameter
  def test_default(self, rtype, pos):
    # for efficiency reasons, eventually instructions will need to be built before processing
    inst = Instruction(rtype, pos)
    self.assertEqual(inst.type, rtype)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.pos,pos)

  # def test_perform(self, package):
  #   pass

if __name__ == '__main__':
  unittest.main()