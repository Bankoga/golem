import utils.object_factory
from components.ordinators.ordinator_provider import ordinator_services
import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.matrix import ordinators

class TestOrdinatorProvider(unittest.TestCase):
  @given(st.sampled_from(sorted(ordinators)))
  def test_get(self, ordinator_id):
    ordinator = ordinator_services.get(ordinator_id, **{})
    self.assertTrue(ordinator.get_id(), ordinator_id)
    
if __name__ == '__main__':
    unittest.main()