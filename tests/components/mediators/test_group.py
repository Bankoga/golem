import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.mediators.group import Group
from components.enums.prop_types import GroupType

from components.enums.module import ModuleType
from components.enums.pos import CtgType
from components.matrix.lineage_registry import LineageRegistry
from components.matrix.channel_registry import ChannelRegistry
from components.vars.data import Lineage
from tests.components.base.mechanisms.test_mechanism import TestMechanism

class TestGroup(TestMechanism):
  def set_up_base(self):
    self.label = 'noise_dwn_inhib'
    self.ctg = CtgType.GROUP
    self.comp_class = Group

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_lineage_registry_api')
    self.lineage_registry = self.registry
    self.lineage = Lineage(golem='arith_brain',matrix='left',module='thalamus', stage='noise_ctrl',group=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.group_type = GroupType.ORGANO
    self.values = [self.registry, self.group_type]
    self.var = tuple(self.values)
    self.baseline = self.values

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = self.comp_class(*self.values,label=self.label)

  def test_get_group_type(self):
    self.assertEqual(self.comp.group_type, self.group_type)
  def test_set_group_type(self):
    with self.assertRaises(RuntimeError):
      self.comp.group_type = self.group_type

if __name__ == '__main__':
  unittest.main()