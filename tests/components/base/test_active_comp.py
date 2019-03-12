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
    self.var = 'Any arbitrary type of object?'
    self.comp = ActiveComp(self.var, item_id=self.label, ctg=self.ctg)

  @given(st.lists(st.one_of(st.text(),st.integers(),st.lists(st.integers()))))
  def test_update(self, new_var):
    self.comp.update(new_var)
    self.comp.var = new_var
    self.assertEqual(self.comp.var, new_var)

  def test_base_set(self):
    self.assertTrue(self.comp.base_set)

  def test_base_var(self):
    self.assertTrue(self.comp.base_set)
    self.assertEqual(self.comp.base_var, self.var)
  
  def test_set_base_var(self):
    with self.assertRaises(RuntimeError):
      self.comp.base_var = 'Does not matter'

  def test_set_base_set(self):
    with self.assertRaises(RuntimeError):
      self.comp.base_set = 'Does not matter'

  def test_reset(self):
    self.comp.update('Things')
    self.comp.reset()
    result = self.comp.var
    self.assertEqual(result,self.var)

if __name__ == '__main__':
  unittest.main()