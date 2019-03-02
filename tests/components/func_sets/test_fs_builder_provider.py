import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.func_sets.fs_builder_provider import fs_services
from data.enums.prop_types import SetType

from data.axioms.configs import proc_ids

from tests.strategies.golem_strats import fg_provider_id
import utils.object_factory

class TestFSBuilderProvider(unittest.TestCase):
  def test_get_specific(self):
    fg_type_id = f'{SetType.GATEWAY}-{proc_ids["glg"]}'
    if (fg_type_id is None):
      with self.assertRaises(ValueError):
        fg = fs_services.get(fg_type_id, **{})
    else:
      parts = fg_type_id.split('-')
      g_type = SetType[parts[0].split('.')[1]]
      if g_type is None:
        with self.assertRaises(ValueError):
          fg = fs_services.get(fg_type_id, **{})
      elif g_type in SetType:
        fg = fs_services.get(fg_type_id, **{})
        self.assertTrue(fg.get_id(), fg_type_id)
      else:
        with self.assertRaises(ValueError):
          fg = fs_services.get(fg_type_id, **{})
  
  @given(fg_provider_id()) # pylint: disable=no-value-for-parameter
  def test_get_arb(self, fg_type_id):
    if (fg_type_id is None):
      with self.assertRaises(ValueError):
        fg = fs_services.get(fg_type_id, **{})
    else:
      parts = fg_type_id.split('-')
      g_type = SetType[parts[0].split('.')[1]]
      if g_type is None:
        with self.assertRaises(ValueError):
          fg = fs_services.get(fg_type_id, **{})
      elif g_type in SetType:
        fg = fs_services.get(fg_type_id, **{})
        self.assertTrue(fg.get_id(), fg_type_id)
      else:
        with self.assertRaises(ValueError):
          fg = fs_services.get(fg_type_id, **{})

if __name__ == '__main__':
  unittest.main()