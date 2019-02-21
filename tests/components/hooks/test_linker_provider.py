# import utils.object_factory
# from components.hooks.linker_provider import services
# import unittest
# from hypothesis import given
# from hypothesis import strategies as st
# from  data.axioms.configs import links

# class TestLinkerProvider(unittest.TestCase):
#   @given(st.sampled_from(links))
#   def test_get(self, link_id):
#     linker = services.get(link_id, **{})
#     self.assertTrue(linker.get_id(), link_id)
    
# if __name__ == '__main__':
#     unittest.main()