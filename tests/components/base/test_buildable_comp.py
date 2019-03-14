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
    self.var = 'Any arbitrary type of object?'
    self.comp = BuildableComp(label=self.label, ctg=self.ctg)

  def test_pre_build(self):
    self.assertFalse(self.comp.is_built)

  def test_set_is_built(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_built = 'Does not matter'

  def test_build(self):
    self.comp.build(self.var)
    self.assertEqual(self.comp.var, self.var)
    self.assertTrue(self.comp.is_built)

  def test_double_build(self):
    self.comp.build(self.var)
    with self.assertRaises(RuntimeError):
      self.comp.build(self.var)

  def test_set_unbuilt_var(self):
    self.comp.var = self.var
    self.assertEqual(self.comp.var, self.var)

  def test_set_built_var(self):
    self.comp.build(self.var)
    with self.assertRaises(RuntimeError):
      self.comp.var = self.var

  def test_get_var(self):
    self.assertEqual(self.comp.var, None)

if __name__ == '__main__':
  unittest.main()