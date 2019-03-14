import unittest

import re

from hypothesis import given
from hypothesis import strategies as st

from components.axioms.props import id_pattern

from tests.strategies.prop_strats import arbitrary_id, arbitrary_invalid_id

from utils.validators.prop_validators import is_valid_id

class TestPropValidators(unittest.TestCase):

  @given(arbitrary_invalid_id()) # pylint: disable=no-value-for-parameter
  def test_is_valid_id_on_arbitrary(self, label):
    result = is_valid_id(label)
    if len(re.findall(id_pattern, label)) == 1:
      self.assertTrue(result)
    else:
      self.assertFalse(result)

  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_is_valid_id(self, label):
    result = is_valid_id(label)
    if len(re.findall(id_pattern, label)) == 1:
      self.assertTrue(result)
    else:
      self.assertFalse(result)

if __name__ == '__main__':
  unittest.main()