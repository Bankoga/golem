import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array_equal, ones

from components.data.conv_shape import ConvShape
from components.enums.pos import CtgType
from components.vars.data import ConvVar
from tests.components.base.test_passive_comp import TestPassiveComp
from tests.strategies.data_strats import valid_resource_data, valid_shape, valid_weights
from utils.pos import Pos


class TestConvShape(TestPassiveComp):

  def setUp(self):
    self.filter_shape = (4,4)
    self.spacing_shape = (1,1)
    self.weights = ones(self.filter_shape)
    self.var = ConvVar(filter_shape=self.filter_shape, spacing_shape=self.spacing_shape,weights=self.weights)
    self.ctg = CtgType.DATA
    self.label = 'TotallyValidId'
    self.comp = ConvShape(self.filter_shape, self.spacing_shape,label=self.label)

  @given(valid_shape(),valid_shape(),valid_weights()) # pylint: disable=no-value-for-parameter
  def test_prepare_args(self, f_shape,s_shape,weights):
    var_args = [f_shape,s_shape,weights]
    expectation = ConvVar(filter_shape=f_shape, spacing_shape=s_shape,weights=weights)
    result = self.comp.prepare_args(*var_args)
    self.assertEqual(result, expectation)
    self.assertEqual(result.filter_shape, f_shape)
    self.assertEqual(result.spacing_shape, s_shape)
    self.assertTrue(array_equal(result.weights, weights))

  def test_get_var(self):
    for i in range(len(self.comp.var)):
      self.assertTrue(array_equal(self.comp.var[i], self.var[i]))

  def test_get_weights(self):
    self.assertTrue(array_equal(self.comp.weights, self.weights))

  def test_get_filter_shape(self):
    self.assertEqual(self.comp.filter_shape, self.filter_shape)

  def test_get_spacing_shape(self):
    self.assertEqual(self.comp.spacing_shape, self.spacing_shape)

  def test_set_weights(self):
    with self.assertRaises(RuntimeError):
      self.comp.weights = 'Does not matter'

  def test_set_filter_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.filter_shape = 'Does not matter'

  def test_set_spacing_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.spacing_shape = 'Does not matter'

if __name__ == '__main__':
  unittest.main()
