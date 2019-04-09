import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from components.vars.data import Lineage
from tests.components.base.test_plastic_comp import TestPlasticComp
from tests.components.base.test_segment import TestSegment
from tests.strategies.data_strats import (valid_resource_data,
                                          valid_resource_data_and_index,
                                          valid_shape,
                                          valid_sz_shape_and_index,
                                          valid_weights)
from tests.strategies.instruction_strats import valid_collector_segment
from tests.strategies.pos_strats import arb_lineage
from utils.pos import Pos
from math import isnan

class TestCollectorSegment(TestPlasticComp,TestSegment):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'dend_abov_a_segment_2'
    self.comp_class = CollectorSegment
    
  def set_up_var(self):
    self.source_lineage = Lineage(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0')
    self.residence_lineage = Lineage(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.lineage = self.residence_lineage
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
    self.comp = self.comp_class(self.value,residence_lineage=self.residence_lineage,source_lineage=self.source_lineage,lineage=self.lineage,source_index=self.source_index,fill_shape=self.fill_shape,label=self.label)

  @given(valid_shape()) # pylint: disable=no-value-for-parameter
  def test_set_fill_shape(self, arb_shape):
    self.comp.fill_shape = arb_shape
    self.assertEqual(self.comp.fill_shape, arb_shape)
    self.assertEqual(self.comp.shape, arb_shape)

  def test_get_source_lineage(self):
    self.assertEqual(self.comp.source_lineage, self.source_lineage)
  @given(arb_lineage()) # pylint: disable=no-value-for-parameter
  def test_set_source_lineage(self, lineage):
    with self.assertRaises(RuntimeError):
      self.comp.source_lineage = lineage
  
  def test_get_collection_chances(self):
    self.assertTrue(array_equal(self.comp.collection_chances, self.default_collection_chances))
  def test_set_collection_chances(self):
    self.comp.collection_chances = self.default_weights/2
    self.assertTrue(array_equal(self.comp.collection_chances, self.default_weights/2))
    self.comp.collection_chances[0][0] = 256
    self.assertTrue(self.comp.collection_chances[0][0], 256)

  @given(st.tuples(st.integers(),st.integers()))
  def test_get_side_szs(self, side_sz):
    x_sz = side_sz
    y_sz = side_sz
    if type(side_sz) is tuple:
      x_sz = side_sz[0]
      y_sz = side_sz[1]
    res_x, res_y = self.comp.get_side_szs(side_sz)
    self.assertEqual(res_x, x_sz)
    self.assertEqual(res_y, y_sz)
  
  def quadrant_helper(self, sz_shape_and_index):
    resource_data, input_ind,side_sz = sz_shape_and_index
    x_sz = side_sz
    y_sz = side_sz
    if type(side_sz) is tuple:
      x_sz = side_sz[0]
      y_sz = side_sz[1]
    x = input_ind[0]
    if len(input_ind) > 1:
      y = input_ind[1]
      expectation = resource_data[x:x+x_sz][y:y+y_sz]
    else:
      expectation = resource_data[x:x+side_sz]
    res = self.comp.extract_quadrant(input_ind,resource_data,side_sz)
    self.assertTrue(array_equal(res, expectation))

  @given(valid_sz_shape_and_index()) # pylint: disable=no-value-for-parameter
  def test_extract_quadrant(self, sz_shape_and_index):
    self.quadrant_helper(sz_shape_and_index)

  @given(valid_resource_data_and_index()) # pylint: disable=no-value-for-parameter
  def test_get_quantity(self, rd_ij):
    data,i,j = rd_ij
    res = self.comp.get_quantity(data, i,j)
    self.assertTrue(0 <= res and not isnan(res))

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_apply(self, resource_data):
    if len(resource_data.shape) != 2:
      with self.assertRaises(RuntimeError):
        res = self.comp.apply(resource_data)
    res = self.comp.apply(resource_data)
    self.assertTrue(res.shape == self.comp.weights.shape)
    for i,row in enumerate(self.comp.weights):
      for j,w in enumerate(row):
        r = res[i][j]
        self.assertTrue(0 <= r and not isnan(r))
        # try:
        rsrc = resource_data[i][j]
        if w > 0 and rsrc > 0:
          if rsrc < w:
            expectation = rsrc
          else:
            expectation = w
        else:
          expectation = 0
        self.assertEqual(r,round(expectation,5))

if __name__ == '__main__':
  unittest.main()

        # quantity = self.get_quantity(x, i)
        # # dist_adj_quantity = quantity - distance_from_source
        # actual = 0
        # if quantity and weight:
        #   actual = min(quantity, weight)
        # actuals.append(actual)