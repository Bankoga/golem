import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.func_groups.fg_builder_provider import fg_services
from data.enums.prop_types import GroupType

from data.axioms.configs import proc_ids

from tests.strategies.golem_strats import fg_provider_id
import utils.object_factory

class TestFGBuilderProvider(unittest.TestCase):
  def test_get_specific(self):
    fg_type_id = f'{GroupType.GATEWAY}-{proc_ids["glg"]}'
    if (fg_type_id is None):
      with self.assertRaises(ValueError):
        fg = fg_services.get(fg_type_id, **{})
    else:
      parts = fg_type_id.split('-')
      g_type = GroupType[parts[0].split('.')[1]]
      if g_type is None:
        with self.assertRaises(ValueError):
          fg = fg_services.get(fg_type_id, **{})
      elif g_type in GroupType:
        fg = fg_services.get(fg_type_id, **{})
        self.assertTrue(fg.get_id(), fg_type_id)
      else:
        with self.assertRaises(ValueError):
          fg = fg_services.get(fg_type_id, **{})
  
  @given(fg_provider_id()) # pylint: disable=no-value-for-parameter
  def test_get_arb(self, fg_type_id):
    if (fg_type_id is None):
      with self.assertRaises(ValueError):
        fg = fg_services.get(fg_type_id, **{})
    else:
      parts = fg_type_id.split('-')
      g_type = parts[0]
      if g_type is None:
        with self.assertRaises(ValueError):
          fg = fg_services.get(fg_type_id, **{})
      elif g_type in GroupType:
        fg = fg_services.get(fg_type_id, **{})
        self.assertTrue(fg.get_id(), fg_type_id)
      else:
        with self.assertRaises(ValueError):
          fg = fg_services.get(fg_type_id, **{})

if __name__ == '__main__':
  unittest.main()