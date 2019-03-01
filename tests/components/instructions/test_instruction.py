import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.enums.prop_types import RuleType
from data.enums.pos import ComponentType
from tests.strategies.enum_strats import ruletype
from tests.strategies.pos_strats import valid_pos

from utils.pos import Pos
from components.instructions.instruction import Instruction

class TestInstruction(unittest.TestCase):
  def setUp(self):
    # self.instruction = Instruction(RuleType.CONV, )
    pass

  @given(ruletype(), valid_pos()) # pylint: disable=no-value-for-parameter
  def test_default(self, rtype, pos):
    # for efficiency reasons, eventually instructions will need to be built before processing
    itm_id = f'{rtype.name}-{pos.get_hash()}' # What is the id of AN instruction in the matrix?
    inst = Instruction(rtype, pos)
    c_lvl = rtype.get_component_type()
    self.assertEqual(inst.get_id(), itm_id)
    self.assertEqual(inst.op_lvl, ComponentType(c_lvl))
    self.assertEqual(inst.ctg_type, rtype)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.pos,pos)

  # def test_perform(self, inputs):
  #   pass

if __name__ == '__main__':
  unittest.main()