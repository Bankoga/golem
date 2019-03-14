import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.workers.worker_comp import WorkerComp
from components.enums.pos import CtgType

from tests.components.base.test_static_comp import TestStaticComp

from tests.strategies.pos_strats import arb_addr

class TestWorkerComp(TestStaticComp):
  def setUp(self):
    self.registry = {}
    self.address = 'm_0-f_0-g_0'
    self.label = 'pr_0'
    self.ctg = CtgType.PACKAGER
    self.reg_item = {
      'address': self.address,
      'pos': None,
      'reg_id': self.label
    }
    self.comp = WorkerComp(label=self.label, ctg=self.ctg)

  def test_pre_registered_state(self):
    self.assertFalse(self.comp.is_registered)
    self.assertIsNone(self.comp.address)
    with self.assertRaises(RuntimeError):
      self.comp.operate()
  
  def test_set_address_post_registration(self):
    self.comp.register(self.registry)
    with self.assertRaises(RuntimeError):
      self.comp.address = 'Anything'

  @given(arb_addr()) # pylint: disable=no-value-for-parameter
  def test_set_address_pre_registration(self, addr):
    self.address = addr

  def test_set_is_registered(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_registered = True

  def test_reg_item(self):
    self.assertEqual(self.comp.reg_item, self.reg_item)
  
  def test_set_reg_item(self):
    with self.assertRaises(RuntimeError):
      self.comp.reg_item['address'] = 'stuff?'

  def test_register(self):
    self.comp.register(self.registry)
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