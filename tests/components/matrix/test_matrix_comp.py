import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import CtgType
from components.matrix.matrix_comp import MatrixComp

from tests.components.base.test_plastic_comp import TestPlasticComp

class TestMatrixComp(TestPlasticComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MATRIX
    self.value = {}
    self.var = tuple([self.value])
    self.comp = MatrixComp(self.value, label=self.label)

if __name__ == '__main__':
  unittest.main()