import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.weighted_comp import WeightedComp
from components.enums.pos import CtgType

from tests.components.base.test_static_comp import TestStaticComp
from tests.strategies.data_strats import valid_shape, valid_weights
from numpy import array_equal, ones

class TestWeightedComp(TestStaticComp):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.INSTRUCTION

  def set_up_defaults(self):
    self.default_num_dim_of_mass = 0
    self.default_shape = tuple([])
    self.default_weights = []
    self.default_is_locked = False

  def set_up_dynamic_props(self):
    pass
  
  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_dynamic_props()
    self.comp = WeightedComp(label=self.label, ctg=self.ctg)

  def test_get_num_dim_of_mass(self):
    self.assertTrue(array_equal(self.comp.num_dim_of_mass, self.default_num_dim_of_mass))
  
  def test_set_num_dim_of_mass(self):
    with self.assertRaises(RuntimeError):
      self.comp.num_dim_of_mass = self.default_num_dim_of_mass

  def test_get_shape(self):
    self.assertTrue(array_equal(self.comp.shape, self.default_shape))
  
  @given(valid_shape()) # pylint: disable=no-value-for-parameter
  def test_set_shape(self, new_shape):
    self.comp.shape = new_shape
    self.assertTrue(array_equal(self.comp.shape, new_shape))
    self.assertTrue(array_equal(self.comp.num_dim_of_mass, len(new_shape)))
    self.assertTrue(array_equal(self.comp.weights, ones(new_shape)))

  def test_get_weights(self):
    self.assertTrue(array_equal(self.comp.weights, self.default_weights))
  
  @given(valid_weights()) # pylint: disable=no-value-for-parameter
  def test_set_weights(self, new_weights):
    self.comp.weights = new_weights
    self.assertTrue(array_equal(self.comp.weights, new_weights))

  def test_get_is_locked(self):
    self.assertTrue(array_equal(self.comp.is_locked, self.default_is_locked))
  
  def test_set_is_locked(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_locked = True

  def test_lock_weights(self):
    self.comp.toggle_lock()
    self.assertTrue(self.comp.is_locked)
    with self.assertRaises(RuntimeError):
      self.comp.weights = self.default_weights
    with self.assertRaises(RuntimeError):
      self.comp.shape = self.default_shape




if __name__ == '__main__':
  unittest.main()