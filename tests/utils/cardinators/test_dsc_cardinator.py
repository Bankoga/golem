import unittest
from hypothesis import given
from hypothesis import strategies as st
import utils.object_factory
from utils.cardinators.dsc_cardinator import DscCardinator
from components.axioms.pos_maps import cardinal_keys
from components.enums.pos import floor_order

class TestDscCardinator(unittest.TestCase):
  
  def setUp(self):
    self.cardinator = DscCardinator()

  def test_init(self):
    self.assertTrue(self.cardinator.get_id(), 'dsc')
    self.assertTrue(self.cardinator.get_direction(), 'dsc')

  @given(st.integers(min_value=0,max_value=len(floor_order)-1), st.just(len(floor_order)))
  def test_get_valid_ord_index(self, ind, sz):
    self.assertEqual(self.cardinator.get_card_index(ind,sz), (sz - ind - 1))
  
  @given(st.integers(min_value=len(floor_order)), st.just(len(floor_order)))
  def test_get_invalid_large_ord_index(self, ind, sz):
    with self.assertRaises(ValueError):
      self.cardinator.get_card_index(ind,sz)

  @given(st.integers(max_value=-1), st.just(len(floor_order)))
  def test_get_invalid_neg_ord_index(self, ind, sz):
    with self.assertRaises(ValueError):
      self.cardinator.get_card_index(ind,sz)

if __name__ == '__main__':
    unittest.main()