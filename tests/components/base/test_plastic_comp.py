import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.plastic_comp import PlasticComp
from components.enums.prop_types import CtgType
from tests.components.base.test_passive_comp import TestPassiveComp
from tests.components.base.test_weighted_comp import TestWeightedComp

class TestPlasticComp(TestPassiveComp,TestWeightedComp):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.INSTRUCTION

  def set_up_defaults(self):
    self.default_num_dim_of_mass = 0
    self.default_shape = None
    self.default_weights = []
    self.default_is_locked = False

  def set_up_var(self):
    self.value = 'Any arbitrary type of object?'
    self.var = tuple([self.value])

  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_var()
    self.comp = PlasticComp(self.value, label=self.label, ctg=self.ctg)

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
    self.comp.baseline = 'A baseline!'
    self.comp.update('Things')
    self.comp.reset()
    self.assertEqual(self.comp.var,tuple(['A baseline!']))

if __name__ == '__main__':
  unittest.main()