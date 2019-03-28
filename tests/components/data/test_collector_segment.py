import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from tests.components.base.test_plastic_comp import TestPlasticComp
from tests.strategies.data_strats import valid_resource_data, valid_shape, valid_weights
from utils.pos import Pos

class TestCollectorSegment(TestPlasticComp):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'TotallyValidId'
    
  def set_up_var(self):
    self.fill_shape = (4,4)
    self.weights = ones(self.fill_shape)
    self.values = [self.fill_shape]
    self.var = tuple(self.values)

  def set_up_defaults(self):
    self.default_shape = (4,4)
    self.default_weights = ones(self.default_shape)
    self.default_num_dim_of_mass = len(self.default_shape)
    self.default_is_locked = False

  def set_up_dynamic_props(self):
    self.baseline = self.values

  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_var()
    self.set_up_dynamic_props()
    self.comp = CollectorSegment(self.fill_shape,label=self.label)

  # @given(valid_shape()) # pylint: disable=no-value-for-parameter
  # def test_prepare_var_args(self, f_shape):
  #   var_args = [f_shape]
  #   expectation = tuple([f_shape])
  #   result = self.comp.prepare_var_args(*var_args)
  #   self.assertEqual(result, expectation)
  #   self.assertEqual(result[0], f_shape)
  #   self.assertEqual(self.comp.shape, result[0])

  # def test_get_var(self):
  #   for i in range(len(self.comp.var)):
  #     self.assertTrue(array_equal(self.comp.var[i], self.var[i]))

  # def test_get_fill_shape(self):
  #   self.assertEqual(self.comp.fill_shape, self.fill_shape)

  # def test_set_fill_shape(self):
  #   with self.assertRaises(RuntimeError):
  #     self.comp.fill_shape = 'Does not matter'

  # @given(valid_shape()) # pylint: disable=no-value-for-parameter
  # def test_update(self,f_shape):
  #   self.comp.update(f_shape)
  #   self.assertEqual(self.comp.var, tuple([f_shape]))
  #   self.assertEqual(self.comp.weights.shape, f_shape)

  # def test_reset_with_baseline(self):
  #   self.comp.baseline = self.baseline
  #   self.comp.update((8,8))
  #   self.assertTrue(array_equal(self.comp.fill_shape, (8,8)))
  #   self.comp.reset()
  #   self.assertEqual(self.comp.var,tuple(*self.baseline))

if __name__ == '__main__':
  unittest.main()
