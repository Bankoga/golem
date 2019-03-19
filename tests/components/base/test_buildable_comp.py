import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.buildable_comp import BuildableComp
from components.enums.prop_types import CtgType
from tests.components.base.test_passive_comp import TestPassiveComp

class TestBuildableComp(TestPassiveComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.FSET
    self.values = [None]
    self.var = tuple(self.values)
    self.comp = BuildableComp(label=self.label, ctg=self.ctg)

  def test_get_var_built(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.var, self.var)

  def test_set_is_built(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_built = 'Does not matter'

  def test_build(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.var, self.var)
    self.assertTrue(self.comp.is_built)

  def test_double_build(self):
    self.comp.build(*self.values)
    with self.assertRaises(RuntimeError):
      self.comp.build(*self.values)

  def test_set_built_var(self):
    self.comp.build(*self.values)
    with self.assertRaises(RuntimeError):
      self.comp.var = self.var

if __name__ == '__main__':
  unittest.main()