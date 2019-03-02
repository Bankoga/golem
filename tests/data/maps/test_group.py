import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.axioms.configs import coder_ids, proc_ids
from data.enums.prop_types import GroupType
from data.maps.group import get_ids

from tests.strategies.prop_strats import package_group

class TestGroup(unittest.TestCase):
  @given(package_group()) # pylint: disable=no-value-for-parameter
  def test_get_ids(self,group_type):
    if group_type is None or group_type is GroupType.UNSET:
      with self.assertRaises(ValueError):
        get_ids(group_type)
    else:
      if 100 < group_type.value and group_type.value > 200:
        expectation = coder_ids
      elif 100 < group_type.value and group_type.value > 200:
        expectation = proc_ids
      else:
        expectation = []
      result = get_ids(group_type)
      self.assertEqual(result, expectation)

if __name__ == '__main__':
  unittest.main()