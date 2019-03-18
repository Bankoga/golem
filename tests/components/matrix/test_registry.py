import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.registry import Registry

from tests.components.matrix.test_matrix_comp import TestMatrixComp
from tests.strategies.var_strats import reg_item_var,reg_item_valid_var

from utils.pos import Pos
from utils.validators.matrix import reg_item_check

class TestRegistry(TestMatrixComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MATRIX
    self.value = {}
    self.var = tuple([self.value])
    self.registry = self.var[0]
    self.comp = Registry(label=self.label)

  def test_registry(self):
    self.assertEqual(self.comp.registry, self.registry)

  @given(st.one_of(st.text(),st.integers(),st.lists(st.integers())))
  def test_set_registry(self, new_var):
    with self.assertRaises(RuntimeError):
      self.comp.registry = new_var

  def add_invalid_item(self,new_item):
    with self.assertRaises(RuntimeError):
      self.comp.add_item(new_item)

  def add_valid_item(self,new_item):
    self.comp.add_item(new_item)
    self.assertTrue(len(self.comp.registry), 1)
    self.comp.remove_item(new_item['reg_id'])

  @given(reg_item_var()) # pylint: disable=no-value-for-parameter
  def test_add_item(self, new_item):
    if reg_item_check(new_item):
      self.add_valid_item(new_item)
    else:
      self.add_invalid_item(new_item)

  def get_item(self, new_item):
    self.comp.add_item(new_item)
    self.assertEqual(self.comp.get_item(new_item['reg_id']), new_item)
    self.comp.remove_item(new_item['reg_id'])

  @given(reg_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_get_item(self, new_item):
    self.get_item(new_item)

  def add_dup_item(self, new_item):
    self.comp.add_item(new_item)
    with self.assertRaises(RuntimeError):
      self.comp.add_item(new_item)
    self.comp.remove_item(new_item['reg_id'])

  @given(reg_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_add_dup_item(self, new_item):
    self.add_dup_item(new_item)
  
  def remove_missing_item(self,old_item):
    with self.assertRaises(RuntimeError):
      self.comp.remove_item(old_item['reg_id'])

  @given(reg_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_remove_missing_item(self,old_item):
    self.remove_missing_item(old_item)

  def remove_item(self, old_item):
    self.comp.add_item(old_item)
    self.comp.remove_item(old_item['reg_id'])
    with self.assertRaises(KeyError):
      self.comp.get_item(old_item['reg_id'])

  @given(reg_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_remove_item(self,old_item):
    self.remove_item(old_item)

if __name__ == '__main__':
  unittest.main()