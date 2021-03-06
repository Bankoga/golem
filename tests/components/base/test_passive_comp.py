import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.passive_comp import PassiveComp
from components.enums.prop_types import CtgType
from tests.components.base.test_static_comp import TestStaticComp

class TestPassiveComp(TestStaticComp):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MODULE

  def set_up_var(self):
    self.value = 'Any arbitrary type of object?'
    self.values = [self.value]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = PassiveComp(self.value, label=self.label, ctg=self.ctg)

  @given(st.lists(st.integers()))
  def test_package_var_args(self, var_args):
    expectation = tuple(var_args)
    result = self.comp.package_var_args(*var_args)
    self.assertEqual(result, expectation)

  @given(st.lists(st.one_of(st.text(),st.integers(),st.lists(st.integers()))))
  def test_update(self, new_var):
    self.comp.update(new_var)
    self.assertEqual(self.comp.var, tuple([new_var]))

  def test_setter_error(self):
    with self.assertRaises(RuntimeError):
      self.comp.setter_error()

  @given(st.one_of(st.text(),st.integers(),st.lists(st.integers())))
  def test_set_var(self, new_var):
    with self.assertRaises(RuntimeError):
      self.comp.var = new_var

  def test_get_var(self):
    self.assertEqual(self.comp.var, self.var)


if __name__ == '__main__':
  unittest.main()