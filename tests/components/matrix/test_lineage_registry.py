import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.lineage_registry import LineageRegistry

from tests.components.matrix.test_registry import TestRegistry
from tests.strategies.var_strats import lineage_item_valid_var, lineage_item_var

from utils.validators.matrix import lineage_item_check

class TestLineageRegistry(TestRegistry):
  def setUp(self):
    self.label = 'GlobalMailRegistry'
    self.ctg = CtgType.MATRIX
    self.value = {}
    self.var = tuple([self.value])
    self.registry = self.var[0]
    self.comp = LineageRegistry(label=self.label)
  
  @given(st.one_of(lineage_item_var(), lineage_item_valid_var())) # pylint: disable=no-value-for-parameter
  def test_add_item(self, new_item):
    if lineage_item_check(new_item):
      self.add_valid_item(new_item)
    else:
      self.add_invalid_item(new_item)

  @given(lineage_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_get_item(self, new_item):
    self.get_item(new_item)

  @given(lineage_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_add_dup_item(self, new_item):
    self.add_dup_item(new_item)

  @given(lineage_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_remove_missing_item(self,old_item):
    self.remove_missing_item(old_item)

  @given(lineage_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_remove_item(self,old_item):
    self.remove_item(old_item)

  # def test_send_package(self, package):
  #   """
  #   what does it mean to check a package?
  #   Do we require a valid recipient and sender valid in a specified context?
  #   Do we simply do property safety checks?
  #   Is data required?
  #   """
  #   if channel_check(package):
  #     self.test_send_package(package)

if __name__ == '__main__':
  unittest.main()
