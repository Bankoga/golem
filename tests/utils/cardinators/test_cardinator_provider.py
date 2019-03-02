import utils.object_factory
from utils.cardinators.cardinator_provider import cardinator_services
import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.utils import cardinators

class TestCardinatorProvider(unittest.TestCase):
  @given(st.sampled_from(sorted(cardinators)))
  def test_get(self, cardinator_id):
    cardinator = cardinator_services.get(cardinator_id, **{})
    self.assertTrue(cardinator.get_id(), cardinator_id)
    
if __name__ == '__main__':
    unittest.main()