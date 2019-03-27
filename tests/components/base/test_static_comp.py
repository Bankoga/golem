import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.static_comp import StaticComp
from components.enums.prop_types import CtgType
from tests.strategies.pos_strats import ctg_prop
from tests.strategies.prop_strats import arb_label,arbitrary_invalid_label

class TestStaticComp(unittest.TestCase):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.FSET
    self.comp = StaticComp(self.label, self.ctg)

  def set_up_dynamic_props(self):
    pass

  def test_set_defaults(self):
    self.assertTrue(self.comp.set_defaults())

  @given(arbitrary_invalid_label()) # pylint: disable=no-value-for-parameter
  def test_set_invalid_label(self,label):
    with self.assertRaises(ValueError):
      self.comp.label = label

  @given(arb_label()) # pylint: disable=no-value-for-parameter
  def test_set_invalid_ctg(self,ctg):
    with self.assertRaises(ValueError):
      self.comp.ctg = ctg

  @given(arb_label()) # pylint: disable=no-value-for-parameter
  def test_set_label(self, label):
    self.comp.label = label
    self.assertEqual(self.comp.label, label)
  
  @given(ctg_prop()) # pylint: disable=no-value-for-parameter
  def test_set_ctg(self, ctg):
    self.comp.ctg = ctg
    self.assertEqual(self.comp.ctg, ctg)

  def test_get_label(self):
    self.assertEqual(self.comp.label, self.label)

  def test_get_ctg(self):
    self.assertEqual(self.comp.ctg, self.ctg)

if __name__ == '__main__':
  unittest.main()