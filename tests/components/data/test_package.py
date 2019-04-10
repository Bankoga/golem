import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.data.package import Package
from components.vars.data import Lineage
from tests.components.base.test_passive_comp import TestPassiveComp
from components.enums.pos import CtgType
from tests.strategies.data_strats import valid_resource_data 
from tests.strategies.pos_strats import arb_lineage

class TestPackage(TestPassiveComp):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.DATA

  def set_up_var(self):
    self.data = 'Any arbitrary type of object?'
    self.sender = Lineage(golem='a',matrix='l',module='glg', stage='prim', group='assoc_from')
    self.recipient = Lineage(golem='a',matrix='b',module='vis_a')
    self.values = [self.data,self.recipient,self.sender]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = Package(*self.values, label=self.label)

  def test_get_recipient(self):
    self.assertEqual(self.comp.recipient, self.recipient)
  @given(arb_lineage()) # pylint: disable=no-value-for-parameter
  def test_set_recipient(self, recipient):
    with self.assertRaises(RuntimeError):
      self.comp.recipient = recipient

  def test_get_data(self):
    self.assertEqual(self.comp.data, self.data)
  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_set_data(self, data):
    with self.assertRaises(RuntimeError):
      self.comp.data = data

  def test_get_sender(self):
    self.assertEqual(self.comp.sender, self.sender)
  @given(arb_lineage()) # pylint: disable=no-value-for-parameter
  def test_set_sender(self, sender):
    with self.assertRaises(RuntimeError):
      self.comp.sender = sender

if __name__ == '__main__':
  unittest.main()