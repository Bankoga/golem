import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.mechanisms.mediators.mediator import Mediator
from components.enums.pos import CtgType
from components.matrix.lineage_registry import LineageRegistry
from components.matrix.channel_registry import ChannelRegistry
from components.vars.data import Lineage
from tests.components.base.mechanisms.test_mechanism import TestMechanism

class TestMediator(TestMechanism):
  def set_up_base(self):
    self.label = 'glg'
    self.ctg = CtgType.FSET
    self.comp_class = Mediator

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_lineage_registry_api')
    self.channel_registry = ChannelRegistry(label='global_channel_registry_api')
    self.lineage_registry = self.registry
    self.sender = Lineage(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from')
    self.lineage = Lineage(golem='a',matrix='l',func_set='glg')
    self.recipient = Lineage(golem='a',matrix='l',func_set='vis_a')
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.values = [self.registry, self.channel_registry]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = self.comp_class(*self.values, label=self.label, ctg=self.ctg)

  def test_get_lineage_registry(self):
    self.assertEqual(self.comp.lineage_registry, self.lineage_registry)
  def test_set_lineage_registry(self):
    with self.assertRaises(RuntimeError):
      self.comp.lineage_registry = self.lineage_registry

  def test_get_channel_registry(self):
    self.assertEqual(self.comp.channel_registry, self.channel_registry)
  def test_set_channel_registry(self):
    with self.assertRaises(RuntimeError):
      self.comp.channel_registry = self.channel_registry

if __name__ == '__main__':
  unittest.main()
