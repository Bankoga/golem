import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.active_comp import ActiveComp
from components.enums.prop_types import CtgType
from tests.components.base.test_passive_comp import TestPassiveComp

class TestActiveComp(TestPassiveComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.FSET
    self.value = 'Any arbitrary type of object?'
    self.var = tuple([self.value])
    self.comp = ActiveComp(self.value, label=self.label, ctg=self.ctg)

  def test_baseline(self):
    self.assertFalse(self.comp.baseline)

  @given(st.tuples(st.one_of(st.text(),st.integers(),st.lists(st.integers()))))
  def test_use_baseline(self, new_var):
    if not new_var:
      with self.assertRaises(RuntimeError):
        self.comp.baseline = new_var
    else:
      self.baseline = new_var
      self.assertEqual(self.baseline, new_var)

  def test_reset_without_baseline(self):
    with self.assertRaises(RuntimeError):
      self.comp.reset()

  def test_reset_with_baseline(self):
    self.comp.baseline = self.value
    self.comp.update('Things')
    self.comp.reset()
    self.assertEqual(self.comp.var,self.var)

if __name__ == '__main__':
  unittest.main()