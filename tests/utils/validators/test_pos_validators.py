import unittest

import re

from hypothesis import given
from hypothesis import strategies as st

from data.enums.pos import CtgType

from tests.strategies.pos_strats import ctg_prop
from tests.strategies.prop_strats import arbitrary_invalid_id

from utils.validators.pos_validators import is_valid_ctg

class TestPosValidators(unittest.TestCase):

  @given(arbitrary_invalid_id()) # pylint: disable=no-value-for-parameter
  def test_is_valid_ctg_on_id(self, itm_id):
    result = is_valid_ctg(itm_id)
    if itm_id in CtgType:
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

if __name__ == '__main__':
  unittest.main()