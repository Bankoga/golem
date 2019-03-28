import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.vars.data import Address
from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from tests.components.base.test_plastic_comp import TestPlasticComp
from tests.strategies.data_strats import valid_resource_data, valid_shape, valid_weights
from utils.pos import Pos
from tests.strategies.pos_strats import arb_addr

class TestCollectorSegment(TestPlasticComp):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'dend_abov_a_segment_2'
    
  def set_up_var(self):
    self.address = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.source_index = (0,0)
    self.fill_shape = (4,4)
    self.weights = ones(self.fill_shape)
    self.values = [self.address, self.source_index, self.fill_shape]
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
    self.comp = CollectorSegment(self.address,self.source_index,self.fill_shape,label=self.label)

  @given(arb_addr(), valid_shape(), valid_shape()) # pylint: disable=no-value-for-parameter
  def test_prepare_var_args(self, address, source_index, f_shape):
    var_args = [address, source_index, f_shape]
    expectation = tuple(var_args)
    result = self.comp.prepare_var_args(*var_args)
    self.assertEqual(result, expectation)
    self.assertEqual(result[2], f_shape)
    self.assertEqual(self.comp.shape, result[2])

  def test_get_var(self):
    for i in range(len(self.comp.var)):
      self.assertTrue(array_equal(self.comp.var[i], self.var[i]))

  def test_get_address(self):
    self.assertEqual(self.comp.address, self.address)
  def test_set_address(self):
    with self.assertRaises(RuntimeError):
      self.comp.address = 'Does not matter'

  def test_get_source_index(self):
    self.assertEqual(self.comp.source_index, self.source_index)
  def test_set_source_index(self):
    with self.assertRaises(RuntimeError):
      self.comp.source_index = 'Does not matter'

  def test_get_fill_shape(self):
    self.assertEqual(self.comp.fill_shape, self.fill_shape)
  def test_set_fill_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.fill_shape = 'Does not matter'

  @given(arb_addr(), valid_shape(), valid_shape()) # pylint: disable=no-value-for-parameter
  def test_update(self,address, source_index, f_shape):
    self.comp.update(address, source_index,f_shape)
    self.assertEqual(self.comp.var, tuple([address,source_index,f_shape]))
    self.assertEqual(self.comp.weights.shape, f_shape)

  @given(arb_addr(), valid_shape(), valid_shape()) # pylint: disable=no-value-for-parameter
  def test_reset_with_baseline(self,address, source_index, f_shape):
    self.comp = CollectorSegment(self.address,self.source_index,self.fill_shape,label=self.label)
    self.comp.baseline = self.baseline
    self.comp.update(address,source_index,f_shape)
    self.assertTrue(array_equal(self.comp.fill_shape, f_shape))
    self.comp.reset()
    self.assertEqual(self.comp.var,tuple(self.baseline))

if __name__ == '__main__':
  unittest.main()
