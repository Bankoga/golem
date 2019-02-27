# import utils.object_factory
# from components.func_groups.fg_builder_provider import fg_services
# import unittest
# from hypothesis import given
# from hypothesis import strategies as st

# from tests.strategies.group_strats import datapack_group
# TODO: EVENTUALLY HAVE A COMPONENT PROVIDER THAT HITS ALL OTHER SUB PROVIDERS
# class TestFGBuilderProvider(unittest.TestCase):
#   @given(datapack_group())
#   def test_get(self, fg_type_id):
#     fg = fg_services.get(fg_type_id, **{})
#     self.assertTrue(fg.get_id(), fg_type_id)
    
# if __name__ == '__main__':
#     unittest.main()