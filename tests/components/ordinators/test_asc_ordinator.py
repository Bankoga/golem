import unittest
from hypothesis import given
from hypothesis import strategies as st
import utils.object_factory
from components.ordinators.asc_ordinator import AscOrdinator
from data.axioms.pos_maps import direction_keys, floor_order

class TestAscOrdinator(unittest.TestCase):
  
  def setUp(self):
    self.ordinator = AscOrdinator()

  def test_init(self):
    self.assertTrue(self.ordinator.get_id(), 'asc')
    self.assertTrue(self.ordinator.get_direction(), 'asc')

  @given(st.integers(max_value=len(floor_order)-1), st.just(len(floor_order)))
  def test_get_valid_ord_index(self, ind, sz):
    self.assertEqual(self.ordinator.get_ord_index(ind,sz), ind)
  
  @given(st.integers(min_value=len(floor_order)), st.just(len(floor_order)))
  def test_get_invalid_ord_index(self, ind, sz):
    with self.assertRaises(ValueError):
      self.ordinator.get_ord_index(ind,sz)

if __name__ == '__main__':
    unittest.main()