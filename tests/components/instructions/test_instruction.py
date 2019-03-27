import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array_equal

from components.enums.pos import CtgType
from components.enums.prop_types import RuleType
from components.instructions.instruction import Instruction
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from tests.components.base.mechanisms.cogs.test_consumer import TestConsumer
from tests.strategies.data_strats import valid_resource_data
from tests.strategies.pos_strats import valid_pos
from tests.strategies.prop_strats import arb_label, rule_type_prop
from utils.pos import Pos

class TestInstruction(TestConsumer):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.INSTRUCTION

  def set_up_var(self):
    self.registry = AddressRegistry(label='global_address_registry_api')
    self.address = Address(golem='a',matrix='l',func_set='b', stage='a',group='a',packager='p',instruction=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.rule_type = RuleType.CONV
    self.old_data = []
    self.prev_data = []
    self.values = [self.registry, self.rule_type]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    # self.pos = Pos(RuleType.CONV.get_component_type())
    self.comp = Instruction(label=self.label)
    self.comp.build(*self.values)

  @given(st.lists(st.integers()))
  def test_prepare_var_args(self, var_args):
    expectation = tuple(var_args)
    result = self.comp.prepare_var_args(*var_args)
    self.assertEqual(result, expectation)
    self.assertEqual(self.comp.prev_data, self.prev_data)
    self.assertEqual(self.comp.old_data, self.old_data)

  def test_get_old_data(self):
    self.assertEqual(self.comp.old_data, self.old_data)
  
  def test_set_old_data(self):
    with self.assertRaises(RuntimeError):
      self.comp.old_data = self.old_data

  def test_get_prev_data(self):
    self.assertEqual(self.comp.prev_data, self.prev_data)
  
  def test_set_prev_data(self):
    with self.assertRaises(RuntimeError):
      self.comp.prev_data = self.prev_data

  def test_instruction_details(self):
    self.assertTrue(self.comp.instruction_details())
  
  # TODO: Define and implement operate details
  # def test_operate_details(self,inputs):
  #   old_prev = self.comp.prev_data
  #   res = self.comp.operate_details(inputs)
  #   self.assertIn(old_prev, self.comp.old_data)
  #   self.assertEqual(self.comp.prev_data, inputs)

  # @given(arb_label(), rule_type_prop(), valid_pos()) # pylint: disable=no-value-for-parameter
  # def test_default(self, label, rtype, pos):
  #   # for efficiency reasons, eventually instructions will need to be built before processing
  #   # label = f'{rtype.name}-{pos.get_hash()}' # What is the id of AN instruction in the matrix?
  #   inst = Instruction(label, rtype, pos)
  #   c_lvl = rtype.get_component_type()
  #   self.assertEqual(inst.label, label)
  #   self.assertEqual(inst.op_lvl, CtgType(c_lvl))
  #   self.assertEqual(inst.ctg_type, rtype)
  #   self.assertIsNone(inst.curr_shape)
  #   self.assertIsNone(inst.curr_bearing)
  #   self.assertIsNone(inst.curr_pos)
  #   self.assertEqual(inst.pos,pos)

  # def test_build(self):
  #   comp = Instruction(self.label, self.ctg,self.pos)
  #   self.assertFalse(comp.is_built())
  #   comp.build()
  #   self.assertTrue(comp.is_built())
  #   comp.operate()

if __name__ == '__main__':
  unittest.main()
