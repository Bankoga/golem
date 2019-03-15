import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.passive_comp import PassiveComp
from components.enums.prop_types import CtgType
from tests.components.base.test_static_comp import TestStaticComp

class TestPassiveComp(TestStaticComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.FSET
    self.var = 'Any arbitrary type of object?'
    self.comp = PassiveComp(self.var, label=self.label, ctg=self.ctg)

  @given(st.one_of(st.text(),st.integers(),st.lists(st.integers())))
  def test_set_var(self, new_var):
    with self.assertRaises(RuntimeError):
      self.comp.var = new_var

  def test_get_var(self):
    self.assertEqual(self.comp.var[0], self.var)

if __name__ == '__main__':
  unittest.main()