import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.mediators.module_creator import module_creator_services
from components.enums.prop_types import ModuleType,SuperSet

from components.axioms.configs import proc_ids

from tests.strategies.prop_strats import fs_provider_id
import utils.object_factory

class TestModuleCreator(unittest.TestCase):
  def test_get_specific(self):
    module_type_id = f'{SuperSet.PROC}-{proc_ids["glg"]}'
    if (module_type_id is None):
      with self.assertRaises(ValueError):
        fs = module_creator_services.get(module_type_id, **{})
    else:
      parts = module_type_id.split('-')
      module_type = SuperSet[parts[0].split('.')[1]]
      if module_type is None:
        with self.assertRaises(ValueError):
          fs = module_creator_services.get(module_type_id, **{})
      elif module_type in SuperSet:
        fs = module_creator_services.get(module_type_id, **{})
        self.assertTrue(fs.get_id(), module_type_id)
      else:
        with self.assertRaises(ValueError):
          fs = module_creator_services.get(module_type_id, **{})
  
  @given(fs_provider_id()) # pylint: disable=no-value-for-parameter
  def test_get_arb(self, module_type_id):
    if (module_type_id is None):
      with self.assertRaises(ValueError):
        fs = module_creator_services.get(module_type_id, **{})
    else:
      parts = module_type_id.split('-')
      module_type = SuperSet[parts[0].split('.')[1]]
      if module_type is None:
        with self.assertRaises(ValueError):
          fs = module_creator_services.get(module_type_id, **{})
      elif module_type in SuperSet:
        fs = module_creator_services.get(module_type_id, **{})
        self.assertTrue(fs.get_id(), module_type_id)
      else:
        with self.assertRaises(ValueError):
          fs = module_creator_services.get(module_type_id, **{})

if __name__ == '__main__':
  unittest.main()