import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from components.vars.data import Address
from tests.components.base.test_plastic_comp import TestPlasticComp
from tests.components.base.test_segment import TestSegment
from tests.strategies.data_strats import (valid_resource_data,
                                          valid_resource_data_and_index,
                                          valid_shape,
                                          valid_sz_shape_and_index,
                                          valid_weights)
from tests.strategies.instruction_strats import valid_collector_segment
from tests.strategies.pos_strats import arb_addr
from utils.pos import Pos
from math import isnan

class TestCollectorSegment(TestPlasticComp,TestSegment):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'dend_abov_a_segment_2'
    
  def set_up_var(self):
    self.source_address = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0')
    self.residence_address = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.address = self.residence_address
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
    self.comp = CollectorSegment(self.value,residence_address=self.residence_address,source_address=self.source_address,address=self.address,source_index=self.source_index,fill_shape=self.fill_shape,label=self.label)

  @given(valid_shape()) # pylint: disable=no-value-for-parameter
  def test_set_fill_shape(self, arb_shape):
    self.comp.fill_shape = arb_shape
    self.assertEqual(self.comp.fill_shape, arb_shape)
    self.assertEqual(self.comp.shape, arb_shape)

  def test_get_source_address(self):
    self.assertEqual(self.comp.source_address, self.source_address)
  @given(arb_addr()) # pylint: disable=no-value-for-parameter
  def test_set_source_address(self, addr):
    with self.assertRaises(RuntimeError):
      self.comp.source_address = addr
  
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
    input_shape, input_ind,side_sz = sz_shape_and_index
    x_sz = side_sz
    y_sz = side_sz
    if type(side_sz) is tuple:
      x_sz = side_sz[0]
      y_sz = side_sz[1]
    x = input_ind[0]
    if len(input_ind) > 1:
      y = input_ind[1]
      expectation = input_shape[x:x+x_sz][y:y+y_sz]
    else:
      expectation = input_shape[x:x+side_sz]
    res = self.comp.extract_quadrant(input_ind,input_shape,side_sz)
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
    # conv_quad = self.comp.extract_quadrant(self.source_index, resource_data, coll_sgmnt.fill_shape)
    # expectation = array(coll_sgmnt.weights.shape) #this is a numpy array that is the dot product of the two arrays
    # if coll_sgmnt is None:
    #   with self.assertRaises(AttributeError):
    #     res = self.comp.apply(resource_data)
    res = self.comp.apply(resource_data)
    self.assertTrue(res.shape == self.comp.weights.shape)
    for i in range(len(self.comp.weights)):
      for j in range(len(self.comp.weights[i])):
        r = res[i][j]
        self.assertTrue(0 <= r and not isnan(r))
        try:
          w = weights[i][j]
          rsrc = resource_data[i][j]
          if w > 0 and rsrc > 0:
            if rsrc < w:
              self.assertEqual(r,rsrc)
            else:
              self.assertEqual(r,w)
        except:
          self.assertFalse(r)

if __name__ == '__main__':
  unittest.main()
