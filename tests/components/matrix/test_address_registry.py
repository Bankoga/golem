import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.address_registry import AddressRegistry

from tests.components.matrix.test_registry import TestRegistry

class TestAddressRegistry(TestRegistry):
  def setUp(self):
    self.label = 'GlobalMailRegistry'
    self.ctg = CtgType.MATRIX
    self.var = {}
    self.comp = AddressRegistry(item_id=self.label)

if __name__ == '__main__':
  unittest.main()
