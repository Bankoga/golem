import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.func_groups.fg_builder_provider import fg_services

from tests.strategies.golem_strats import fg_provider_id
import utils.object_factory

class TestFGBuilderProvider(unittest.TestCase):
  @given(fg_provider_id())
  def test_get(self, fg_type_id):
    fg_id = group_ids['glg']
    fg_type = GroupType.SENSOR
    fg = fg_services.get(fg_type_id, **{})
    self.assertTrue(fg.get_id(), fg_type_id)
    
if __name__ == '__main__':
    unittest.main()
