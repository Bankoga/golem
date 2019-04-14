import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.buildable_comp import BuildableComp
from components.enums.prop_types import CtgType
from tests.components.base.test_passive_comp import TestPassiveComp

class TestBuildableComp(TestPassiveComp):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MODULE
    self.comp_class = BuildableComp

  def set_up_var(self):
    self.values = []
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = self.comp_class(label=self.label, ctg=self.ctg)

  def test_set_is_built(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_built = 'Does not matter'

  def test_get_var(self):
    self.assertEqual(self.comp.var, self.var)

  def test_build(self):
    self.comp.build()
    self.assertTrue(self.comp.is_built)

  def test_double_build(self):
    self.comp.build()
    with self.assertRaises(RuntimeError):
      self.comp.build()

  def test_set_built_var(self):
    with self.assertRaises(RuntimeError):
      self.comp.var = self.var

if __name__ == '__main__':
  unittest.main()