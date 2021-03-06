import unittest

import re

from hypothesis import given
from hypothesis import strategies as st

from components.axioms.pos import lineage_pattern
from components.enums.pos import CtgType

from tests.strategies.pos_strats import ctg_prop,arb_lineage
from tests.strategies.prop_strats import arbitrary_invalid_label

from utils.validators.pos_validators import is_valid_ctg,is_valid_lineage

class TestPosValidators(unittest.TestCase):

  @given(arbitrary_invalid_label()) # pylint: disable=no-value-for-parameter
  def test_is_valid_ctg_on_id(self, label):
    result = is_valid_ctg(label)
    if label in CtgType:
      self.assertTrue(result)
    else:
      self.assertFalse(result)

  @given(ctg_prop()) # pylint: disable=no-value-for-parameter
  def test_is_valid_ctg(self, ctg):
    result = is_valid_ctg(ctg)
    if ctg in CtgType:
      self.assertTrue(result)
    else:
      self.assertFalse(result)

  @given(st.one_of(arb_lineage(), arbitrary_invalid_label())) # pylint: disable=no-value-for-parameter
  def test_lineage_check(self, lineage):
    match = re.search(lineage_pattern, lineage)
    if match is None:
      expectation = False
    else:
      expectation = len(match.groups()) == 1
    result = is_valid_lineage(lineage)
    self.assertEqual(result,expectation)
  
if __name__ == '__main__':
  unittest.main()