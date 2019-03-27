import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from components.vars.data import ConvVar
from tests.components.base.test_plastic_comp import TestPlasticComp
from tests.strategies.data_strats import valid_resource_data, valid_shape, valid_weights
from utils.pos import Pos

class TestCollectorSegment(TestPlasticComp):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'TotallyValidId'
    
  def set_up_var(self):
    self.filter_shape = (4,4)
    self.spacing_shape = (1,1)
    self.weights = ones(self.filter_shape)
    self.values = [self.filter_shape,self.spacing_shape]
    self.var = ConvVar(filter_shape=self.filter_shape, spacing_shape=self.spacing_shape)

  def set_up_defaults(self):
    self.default_shape = (tuple([1]))
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
    self.comp = CollectorSegment(self.filter_shape, self.spacing_shape,label=self.label)

  @given(valid_shape(),valid_shape()) # pylint: disable=no-value-for-parameter
  def test_prepare_var_args(self, f_shape,s_shape):
    var_args = [f_shape,s_shape]
    expectation = ConvVar(filter_shape=f_shape, spacing_shape=s_shape)
    result = self.comp.prepare_var_args(*var_args)
    self.assertEqual(result, expectation)
    self.assertEqual(result.filter_shape, f_shape)
    self.assertEqual(result.spacing_shape, s_shape)
    self.assertEqual(self.comp.shape, result.filter_shape)

  def test_get_var(self):
    for i in range(len(self.comp.var)):
      self.assertTrue(array_equal(self.comp.var[i], self.var[i]))

  def test_get_filter_shape(self):
    self.assertEqual(self.comp.filter_shape, self.filter_shape)

  def test_get_spacing_shape(self):
    self.assertEqual(self.comp.spacing_shape, self.spacing_shape)

  def test_set_filter_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.filter_shape = 'Does not matter'

  def test_set_spacing_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.spacing_shape = 'Does not matter'

  @given(valid_shape(),valid_shape()) # pylint: disable=no-value-for-parameter
  def test_update(self,f_shape,s_shape):
    self.comp.update(f_shape,s_shape)
    self.assertEqual(self.comp.var, ConvVar(filter_shape=f_shape,spacing_shape=s_shape))
    self.assertEqual(self.comp.weights.shape, self.comp.filter_shape)

  def test_reset_with_baseline(self):
    self.comp.baseline = self.baseline
    self.comp.update((8,8))
    self.assertTrue(array_equal(self.comp.filter_shape, (8,8)))
    self.comp.reset()
    self.assertEqual(self.comp.var,ConvVar(*self.baseline))

if __name__ == '__main__':
  unittest.main()
