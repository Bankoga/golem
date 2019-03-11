import unittest
from hypothesis import given
from hypothesis import strategies as st
import utils.object_factory
from utils.cardinators.cardinator import Cardinator
from components.axioms.pos_maps import cardinal_keys

class TestCardinator(unittest.TestCase):
  
  @given(st.sampled_from(sorted(cardinal_keys)))
  def test_init(self, arbitrary_direction):
    cardinator = Cardinator(arbitrary_direction)
    self.assertTrue(cardinator.get_id(), arbitrary_direction)
    self.assertTrue(cardinator.get_direction(), arbitrary_direction)
    
if __name__ == '__main__':
    unittest.main()