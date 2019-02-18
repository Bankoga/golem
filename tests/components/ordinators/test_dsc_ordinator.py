import unittest
from hypothesis import given
from hypothesis import strategies as st
import utils.object_factory
from components.ordinators.dsc_ordinator import DscOrdinator
from data.axioms.pos_maps import direction_keys, floor_order

class TestDscOrdinator(unittest.TestCase):
  
  def setUp(self):
    self.ordinator = DscOrdinator()

  def test_init(self):
    self.assertTrue(self.ordinator.get_id(), 'dsc')
    self.assertTrue(self.ordinator.get_direction(), 'dsc')

  @given(st.integers(min_value=0,max_value=len(floor_order)-1), st.just(len(floor_order)))
  def test_get_valid_ord_index(self, ind, sz):
    self.assertEqual(self.ordinator.get_ord_index(ind,sz), (sz - ind - 1))
  
  @given(st.integers(min_value=len(floor_order)), st.just(len(floor_order)))
  def test_get_invalid_large_ord_index(self, ind, sz):
    with self.assertRaises(ValueError):
      self.ordinator.get_ord_index(ind,sz)

  @given(st.integers(max_value=-1), st.just(len(floor_order)))
  def test_get_invalid_neg_ord_index(self, ind, sz):
    with self.assertRaises(ValueError):
      self.ordinator.get_ord_index(ind,sz)

if __name__ == '__main__':
    unittest.main()