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
from tests.components.base.test_segment import TestSegment

class TestCollectorSegment(TestPlasticComp,TestSegment):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'dend_abov_a_segment_2'
    
  def set_up_var(self):
    self.address = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.source_index = (0,0)
    self.fill_shape = (4,4)
    self.weights = ones(self.fill_shape)
    self.value = 'anything'
    self.values = [self.value]
    self.var = tuple(self.values)
    self.baseline = self.values

  def set_up_defaults(self):
    self.default_shape = (4,4)
    self.default_weights = ones(self.default_shape)
    self.default_num_dim_of_mass = len(self.default_shape)
    self.default_is_locked = False
    self.default_collection_chances = ones(self.default_shape)

  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_var()
    self.comp = CollectorSegment(self.value,address=self.address,source_index=self.source_index,fill_shape=self.fill_shape,label=self.label)

  @given(valid_shape()) # pylint: disable=no-value-for-parameter
  def test_set_fill_shape(self, arb_shape):
    self.comp.fill_shape = arb_shape
    self.assertEqual(self.comp.fill_shape, arb_shape)
    self.assertEqual(self.comp.shape, arb_shape)

  def test_get_collection_chances(self):
    self.assertTrue(array_equal(self.comp.collection_chances, self.default_collection_chances))
  
  def test_set_collection_chances(self):
    self.comp.collection_chances = self.default_weights/2
    self.assertTrue(array_equal(self.comp.collection_chances, self.default_weights/2))
    self.comp.collection_chances[0][0] = 256
    self.assertTrue(self.comp.collection_chances[0][0], 256)

if __name__ == '__main__':
  unittest.main()
