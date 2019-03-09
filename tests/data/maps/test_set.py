import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.axioms.configs import coder_ids, proc_ids
from data.enums.prop_types import SuperSet
from data.maps.set import get_ids

from tests.strategies.prop_strats import superset_prop

class TestSet(unittest.TestCase):
  @given(superset_prop()) # pylint: disable=no-value-for-parameter
  def test_get_ids(self,set_type):
    
    if set_type is None or set_type is SuperSet.UNSET:
      with self.assertRaises(ValueError):
        get_ids(set_type)
    else:
      if set_type is SuperSet.CODER:# if 100 < set_type.value and set_type.value < 200:
        expectation = list(coder_ids.values())
      elif set_type is SuperSet.PROC:# elif 200 < set_type.value and set_type.value < 300:
        expectation = list(proc_ids.values())
      else:
        expectation = []
    # if 100 < set_type.value and set_type.value < 200:
    #   expectation = SuperSet.CODER.values[1]
    # elif 200 < set_type.value and set_type.value < 300:
    #   expectation = SuperSet.PROC.values[1]
    # else:
    #   expectation = SuperSet.UNSET.values[1]
      result = get_ids(set_type)
      self.assertTrue(result == expectation)

if __name__ == '__main__':
  unittest.main()