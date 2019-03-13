import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.address_registry import AddressRegistry

from tests.components.matrix.test_registry import TestRegistry
from tests.strategies.var_strats import addr_item_valid_var, addr_item_var

from utils.validators.matrix import addr_item_check

class TestAddressRegistry(TestRegistry):
  def setUp(self):
    self.label = 'GlobalMailRegistry'
    self.ctg = CtgType.MATRIX
    self.var = {}
    self.comp = AddressRegistry(item_id=self.label)
  
  @given(st.one_of(addr_item_var(), addr_item_valid_var())) # pylint: disable=no-value-for-parameter
  def test_add_item(self, new_item):
    if addr_item_check(new_item):
      self.add_valid_item(new_item)
    else:
      self.add_invalid_item(new_item)

  @given(addr_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_get_item(self, new_item):
    self.get_item(new_item)

  @given(addr_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_add_dup_item(self, new_item):
    self.add_dup_item(new_item)

  @given(addr_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_remove_missing_item(self,old_item):
    self.remove_missing_item(old_item)

  @given(addr_item_valid_var()) # pylint: disable=no-value-for-parameter
  def test_remove_item(self,old_item):
    self.remove_item(old_item)

if __name__ == '__main__':
  unittest.main()
