import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.vars.data import Address
from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from tests.components.base.test_passive_comp import TestPassiveComp
from tests.strategies.data_strats import valid_resource_data, valid_shape, valid_weights
from utils.pos import Pos
from tests.strategies.pos_strats import arb_addr
from components.base.segment import Segment

class TestCollectorSegment(TestPassiveComp):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'dend_abov_a_segment_2'
    
  def set_up_var(self):
    self.address = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.source_index = (0,0)
    self.fill_shape = (4,4)
    self.values = [self.address,self.source_index,self.fill_shape]
    self.var = tuple(self.values)

  def set_up_defaults(self):
    self.default_shape = (4,4)

  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_var()
    self.comp = Segment(self.address,self.source_index,self.fill_shape,label=self.label,ctg=self.ctg)

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

if __name__ == '__main__':
  unittest.main()