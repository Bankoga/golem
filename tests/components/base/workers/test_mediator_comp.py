import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.workers.mediator_comp import MediatorComp
from components.enums.pos import CtgType
from components.matrix.address_registry import AddressRegistry
from components.matrix.channel_registry import ChannelRegistry
from components.vars.data import Address
from tests.components.base.workers.test_worker_comp import TestWorkerComp

class TestMediatorComp(TestWorkerComp):
  def setUp(self):
    self.registry = AddressRegistry(label='global_address_registry_api')
    self.channel_registry = ChannelRegistry(label='global_channel_registry_api')
    self.address_registry = self.registry
    self.sender = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from')
    self.address = Address(golem='a',matrix='l',func_set='glg')
    self.recipient = Address(golem='a',matrix='l',func_set='vis_a')
    self.label = 'glg'
    self.ctg = CtgType.FSET
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.values = [self.registry, self.channel_registry]
    self.var = tuple(self.values)
    self.comp = MediatorComp(label=self.label, ctg=self.ctg)
    self.comp.build(*self.values)

  def test_get_address_registry(self):
    self.assertEqual(self.comp.address_registry, self.address_registry)

  def test_set_address_registry(self):
    with self.assertRaises(RuntimeError):
      self.comp.address_registry = self.address_registry

  def test_get_channel_registry(self):
    self.assertEqual(self.comp.channel_registry, self.channel_registry)

  def test_set_channel_registry(self):
    with self.assertRaises(RuntimeError):
      self.comp.channel_registry = self.channel_registry

if __name__ == '__main__':
  unittest.main()
