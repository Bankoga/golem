import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.registry import Registry

from tests.components.matrix.test_matrix_comp import TestMatrixComp

class TestRegistry(TestMatrixComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MATRIX
    self.var = {}
    self.comp = Registry(item_id=self.label)

  def add_item(self, new_item):
    pass
  
  def remove_item(self,item_key):
    pass

if __name__ == '__main__':
  unittest.main()