# import unittest
# from hypothesis import given
# from hypothesis import strategies as st
# import utils.object_factory
# from components.ordinators.ordinator import Ordinator
# from data.axioms.pos_maps import direction_keys

# class TestOrdinator(unittest.TestCase):
  
#   @given(st.sampled_from(sorted(direction_keys)))
#   def test_init(self, arbitrary_direction):
#     ordinator = Ordinator(arbitrary_direction)
#     self.assertTrue(ordinator.get_id(), arbitrary_direction)
#     self.assertTrue(ordinator.get_direction(), arbitrary_direction)
    
# if __name__ == '__main__':
#     unittest.main()