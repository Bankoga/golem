import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.matrix.address_registry import AddressRegistry
from components.base.workers.worker_comp import WorkerComp
from components.enums.pos import CtgType
from components.vars.data import Address

from tests.components.base.test_buildable_comp import TestBuildableComp

from tests.strategies.matrix_strats import addr_reg
from tests.strategies.pos_strats import arb_addr

class TestWorkerComp(TestBuildableComp):
  def setUp(self):
    self.registry = AddressRegistry(label='global_registry')
    self.address = Address(golem='a',matrix='l',func_set='b')
    self.label = 'pr_0'
    self.ctg = CtgType.PACKAGER
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.values = [self.registry]
    self.var = tuple(self.values)
    self.comp = WorkerComp(label=self.label, ctg=self.ctg)

  def test_get_registry(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.registry, self.var[0])

  @given(st.one_of(addr_reg(), st.integers())) # pylint: disable=no-value-for-parameter
  def test_set_registry(self, possible_reg):
    if type(possible_reg) == AddressRegistry:
      self.comp.registry = possible_reg
      self.assertEqual(self.comp.registry, possible_reg)
    else:
      with self.assertRaises(RuntimeError):
        self.comp.registry = possible_reg

  def test_pre_registered_state(self):
    self.assertFalse(self.comp.is_registered)
    self.assertIsNone(self.comp.address)
    with self.assertRaises(RuntimeError):
      self.comp.operate()

  def test_set_address_post_registration(self):
    self.comp.build(*self.values)
    self.comp.register(self.address)
    with self.assertRaises(RuntimeError):
      self.comp.address = 'Anything'

  @given(arb_addr()) # pylint: disable=no-value-for-parameter
  def test_set_address_pre_registration(self, addr):
    self.address = addr

  def test_set_is_registered(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_registered = True

  def test_reg_item(self):
    self.comp.build(*self.values)
    self.comp.register(self.address)
    self.maxDiff = None
    self.assertEqual(self.comp.reg_item, self.reg_item)
  
  def test_set_reg_item(self):
    with self.assertRaises(RuntimeError):
      self.comp.reg_item = {}

  def test_register(self):
    self.comp.build(*self.values)
    self.comp.register(self.address)
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

  def test_build_with_data(self):
    self.comp.build(*self.values, address=self.address)
    self.assertEqual(self.comp.var, self.var)
    self.assertTrue(self.comp.is_built)

if __name__ == '__main__':
  unittest.main()