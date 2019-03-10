import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.passive_comp import PassiveComp
from data.enums.prop_types import CtgType
from tests.components.base.test_static_comp import TestStaticComp

class TestPassiveComp(TestStaticComp):
  def setUp(self):
    self.valid_id = 'TotallyValidId'
    self.valid_ctg = CtgType.FSET
    self.var = 'Any arbitrary type of object?'
    self.comp = PassiveComp(self.var, item_id=self.valid_id, ctg=self.valid_ctg)

  @given(st.one_of(st.text(),st.integers(),st.lists(st.integers())))
  def test_set_var(self, new_var):
    self.comp.set_var(new_var)
    self.assertEqual(self.comp.get_var(), new_var)

  def test_get_var(self):
    self.assertEqual(self.comp.get_var(), self.var)

if __name__ == '__main__':
  unittest.main()