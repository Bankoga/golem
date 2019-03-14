import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.static_comp import StaticComp
from components.enums.prop_types import CtgType
from tests.strategies.pos_strats import ctg_prop
from tests.strategies.prop_strats import arbitrary_id,arbitrary_invalid_id

class TestStaticComp(unittest.TestCase):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.FSET
    self.comp = StaticComp(self.label, self.ctg)

  @given(arbitrary_invalid_id()) # pylint: disable=no-value-for-parameter
  def test_set_invalid_id(self,label):
    with self.assertRaises(ValueError):
      self.comp.label = label

  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_set_invalid_ctg(self,ctg):
    with self.assertRaises(ValueError):
      self.comp.ctg = ctg

  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
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