import unittest
from math import isnan

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from tests.strategies.data_strats import valid_resource_data_and_index,valid_sz_shape_and_index
from utils.helpers.arrayer import extract_quadrant, get_quantity, get_sizes


class TestArrayer(unittest.TestCase):

  @given(st.tuples(st.integers(),st.integers()))
  def test_get_sizes(self, shape):
    x_sz = shape
    y_sz = shape
    if type(shape) is tuple:
      x_sz = shape[0]
      y_sz = shape[1]
    res_x, res_y = get_sizes(shape)
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
    res = extract_quadrant(input_ind,resource_data,side_sz)
    self.assertTrue(array_equal(res, expectation))

  @given(valid_sz_shape_and_index()) # pylint: disable=no-value-for-parameter
  def test_extract_quadrant(self, sz_shape_and_index):
    self.quadrant_helper(sz_shape_and_index)

  @given(valid_resource_data_and_index()) # pylint: disable=no-value-for-parameter
  def test_get_quantity(self, rd_ij):
    data,i,j = rd_ij
    res = get_quantity(data, i,j)
    self.assertTrue(0 <= res and not isnan(res))

if __name__ == '__main__':
  unittest.main()
