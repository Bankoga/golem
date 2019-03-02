import unittest
from hypothesis import given
from hypothesis import strategies as st
import utils.object_factory
from utils.cardinators.asc_cardinator import AscCardinator
from data.axioms.pos_maps import cardinal_keys, floor_order

class TestAscCardinator(unittest.TestCase):
  
  def setUp(self):
    self.cardinator = AscCardinator()

  def test_init(self):
    self.assertTrue(self.cardinator.get_id(), 'asc')
    self.assertTrue(self.cardinator.get_direction(), 'asc')

  @given(st.integers(min_value=0,max_value=len(floor_order)-1), st.just(len(floor_order)))
  def test_get_valid_ord_index(self, ind, sz):
    self.assertEqual(self.cardinator.get_card_index(ind,sz), ind)
  
  @given(st.integers(min_value=len(floor_order)), st.just(len(floor_order)))
  def test_get_invalid_ord_index(self, ind, sz):
    with self.assertRaises(ValueError):
      self.cardinator.get_card_index(ind,sz)

  @given(st.integers(max_value=-1), st.just(len(floor_order)))
  def test_get_invalid_neg_ord_index(self, ind, sz):
    with self.assertRaises(ValueError):
      self.cardinator.get_card_index(ind,sz)

if __name__ == '__main__':
    unittest.main()