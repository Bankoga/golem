import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.enums.prop_types import RuleType
from data.enums.pos import CtgType
from tests.strategies.prop_strats import rule_type_prop, arbitrary_id
from tests.strategies.pos_strats import valid_pos
from tests.strategies.packing_strats import valid_resource_data

from utils.pos import Pos
from components.instructions.instruction import Instruction

from tests.components.base.test_component import TestComponent

from numpy import array_equal

class TestInstruction(TestComponent):
  def setUp(self):
    self.valid_c_id = 'TotallyValidId'
    self.valid_c_type = RuleType.CONV
    self.pos = Pos(RuleType.CONV.get_component_type())
    self.comp = Instruction(self.valid_c_id,self.valid_c_type,self.pos)

  @given(arbitrary_id(), rule_type_prop(), valid_pos()) # pylint: disable=no-value-for-parameter
  def test_default(self, itm_id, rtype, pos):
    # for efficiency reasons, eventually instructions will need to be built before processing
    # itm_id = f'{rtype.name}-{pos.get_hash()}' # What is the id of AN instruction in the matrix?
    inst = Instruction(itm_id, rtype, pos)
    c_lvl = rtype.get_component_type()
    self.assertEqual(inst.get_id(), itm_id)
    self.assertEqual(inst.op_lvl, CtgType(c_lvl))
    self.assertEqual(inst.ctg_type, rtype)
    self.assertIsNone(inst.curr_shape)
    self.assertIsNone(inst.curr_bearing)
    self.assertIsNone(inst.curr_pos)
    self.assertEqual(inst.pos,pos)

  def test_build(self):
    comp = Instruction(self.valid_c_id, self.valid_c_type,self.pos)
    self.assertFalse(comp.is_built())
    comp.build()
    self.assertTrue(comp.is_built())
    comp.operate()

if __name__ == '__main__':
  unittest.main()