# import unittest
# from hypothesis import given
# from hypothesis import strategies as st
# import utils.object_factory
# from components.func_groups.group import Group
# from data.axioms.configs import group_types

# class TestGroup(unittest.TestCase):
  
#   @given(st.sampled_from(sorted(group_types)))
#   def test_init(self, arbitrary_direction):
#     group = Group(arbitrary_direction)
#     self.assertTrue(ordinator.get_id(), arbitrary_direction)
#     self.assertTrue(ordinator.get_direction(), arbitrary_direction)
    
# if __name__ == '__main__':
#     unittest.main()