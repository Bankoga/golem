import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.mediators.fs_builder_provider import fs_services
from components.enums.prop_types import FuncSetType,SuperSet

from components.axioms.configs import proc_ids

from tests.strategies.prop_strats import fs_provider_id
import utils.object_factory

class TestFSBuilderProvider(unittest.TestCase):
  def test_get_specific(self):
    fs_type_id = f'{SuperSet.PROC}-{proc_ids["glg"]}'
    if (fs_type_id is None):
      with self.assertRaises(ValueError):
        fs = fs_services.get(fs_type_id, **{})
    else:
      parts = fs_type_id.split('-')
      fs_type = SuperSet[parts[0].split('.')[1]]
      if fs_type is None:
        with self.assertRaises(ValueError):
          fs = fs_services.get(fs_type_id, **{})
      elif fs_type in SuperSet:
        fs = fs_services.get(fs_type_id, **{})
        self.assertTrue(fs.get_id(), fs_type_id)
      else:
        with self.assertRaises(ValueError):
          fs = fs_services.get(fs_type_id, **{})
  
  @given(fs_provider_id()) # pylint: disable=no-value-for-parameter
  def test_get_arb(self, fs_type_id):
    if (fs_type_id is None):
      with self.assertRaises(ValueError):
        fs = fs_services.get(fs_type_id, **{})
    else:
      parts = fs_type_id.split('-')
      fs_type = SuperSet[parts[0].split('.')[1]]
      if fs_type is None:
        with self.assertRaises(ValueError):
          fs = fs_services.get(fs_type_id, **{})
      elif fs_type in SuperSet:
        fs = fs_services.get(fs_type_id, **{})
        self.assertTrue(fs.get_id(), fs_type_id)
      else:
        with self.assertRaises(ValueError):
          fs = fs_services.get(fs_type_id, **{})

if __name__ == '__main__':
  unittest.main()