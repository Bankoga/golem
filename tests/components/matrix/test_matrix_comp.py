import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.matrix_comp import MatrixComp

from tests.components.base.test_active_comp import TestActiveComp

class TestMatrixComp(TestActiveComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MATRIX
    self.var = {}
    self.comp = MatrixComp(self.var, item_id=self.label)

if __name__ == '__main__':
  unittest.main()