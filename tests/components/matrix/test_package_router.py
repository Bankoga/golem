import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.package_router import PackageRouter

from tests.components.matrix.test_matrix_comp import TestMatrixComp

class TestPackageRouter(TestMatrixComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MATRIX
    self.var = {}
    self.comp = PackageRouter(item_id=self.label)

if __name__ == '__main__':
  unittest.main()
