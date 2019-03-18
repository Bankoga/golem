import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.matrix.address_registry import AddressRegistry
from components.base.workers.worker_comp import WorkerComp
from components.enums.pos import CtgType
from components.vars.data import Address

from tests.components.base.test_active_comp import TestActiveComp

from tests.strategies.pos_strats import arb_addr

class TestWorkerComp(TestActiveComp):
  def setUp(self):
    self.registry = AddressRegistry(label='global_registry')
    self.address = Address(golem='a',matrix='l',func_set='b')
    self.label = 'pr_0'
    self.ctg = CtgType.PACKAGER
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.comp = WorkerComp(label=self.label, ctg=self.ctg)

  def test_pre_registered_state(self):
    self.assertFalse(self.comp.is_registered)
    self.assertIsNone(self.comp.address)
    with self.assertRaises(RuntimeError):
      self.comp.operate()
  
  def test_set_address_post_registration(self):
    self.comp.register(self.address,self.registry)
    with self.assertRaises(RuntimeError):
      self.comp.address = 'Anything'

  @given(arb_addr()) # pylint: disable=no-value-for-parameter
  def test_set_address_pre_registration(self, addr):
    self.address = addr

  def test_set_is_registered(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_registered = True

  def test_reg_item(self):
    self.comp.register(self.address, self.registry)
    self.assertEqual(self.comp.reg_item, self.reg_item)
  
  def test_set_reg_item(self):
    with self.assertRaises(RuntimeError):
      self.comp.reg_item = {}

  def test_register(self):
    self.comp.register(self.address,self.registry)
    """
    For every worker, what needs to be registered?
    successful registration means
    - that a registry item has been added to itself
    - that the registry indicated has had the generated reg item added to it
    - that it is ready for operation! (does this mean it is ready to receive packages? yes)
    """
    self.assertTrue(self.comp.is_registered)

  # def test_operate(self):
  #   pass

if __name__ == '__main__':
  unittest.main()