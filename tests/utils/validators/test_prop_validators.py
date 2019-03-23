import unittest

import re

from hypothesis import given
from hypothesis import strategies as st

from components.axioms.props import label_pattern

from tests.strategies.prop_strats import arbitrary_id, arbitrary_invalid_label

from utils.validators.prop_validators import is_valid_label

class TestPropValidators(unittest.TestCase):

  @given(arbitrary_invalid_label()) # pylint: disable=no-value-for-parameter
  def test_is_valid_label_on_arbitrary(self, label):
    result = is_valid_label(label)
    if len(re.findall(label_pattern, label)) == 1:
      self.assertTrue(result)
    else:
      self.assertFalse(result)

  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_is_valid_label(self, label):
    result = is_valid_label(label)
    if len(re.findall(label_pattern, label)) == 1:
      self.assertTrue(result)
    else:
      self.assertFalse(result)

if __name__ == '__main__':
  unittest.main()