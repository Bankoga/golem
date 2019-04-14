import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.vars.data import Lineage
from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from tests.components.base.test_static_comp import TestStaticComp
from tests.strategies.data_strats import valid_resource_data, valid_shape, valid_weights
from utils.pos import Pos
from tests.strategies.pos_strats import arb_lineage
from components.base.segment import Segment

class TestSegment(TestStaticComp):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'dend_abov_a_segment_2'
    
  def set_up_var(self):
    self.residence_lineage = Lineage(golem='a',matrix='l',module='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.source_lineage = Lineage(golem='a',matrix='l',module='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.source_index = (0,0)
    self.fill_shape = (4,4)
    self.values = []
    self.var = tuple(self.values)

  def set_up_defaults(self):
    self.default_shape = (4,4)

  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_var()
    self.comp = Segment(residence_lineage=self.residence_lineage,source_lineage=self.source_lineage,source_index=self.source_index,fill_shape=self.fill_shape,label=self.label,ctg=self.ctg)

  def test_get_residence_lineage(self):
    self.assertEqual(self.comp.source_lineage, self.source_lineage)
  @given(arb_lineage()) # pylint: disable=no-value-for-parameter
  def test_set_residence_lineage(self, lineage):
    with self.assertRaises(RuntimeError):
      self.comp.source_lineage = lineage

  def test_get_source_lineage(self):
    self.assertEqual(self.comp.source_lineage, self.source_lineage)
  @given(arb_lineage()) # pylint: disable=no-value-for-parameter
  def test_set_source_lineage(self, lineage):
    with self.assertRaises(RuntimeError):
      self.comp.source_lineage = lineage

  def test_get_source_index(self):
    self.assertEqual(self.comp.source_index, self.source_index)
  def test_set_source_index(self):
    with self.assertRaises(RuntimeError):
      self.comp.source_index = 'Does not matter'

  def test_get_fill_shape(self):
    self.assertEqual(self.comp.fill_shape, self.fill_shape)
  @given(valid_shape()) # pylint: disable=no-value-for-parameter
  def test_set_fill_shape(self, arb_shape):
    self.comp.fill_shape = arb_shape
    self.assertEqual(self.comp.fill_shape, arb_shape)

if __name__ == '__main__':
  unittest.main()