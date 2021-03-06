import unittest

from hypothesis import given
from hypothesis import strategies as st

from numpy import array_equal

from components.vars.misc import reg_keys, lineage_keys, channel_keys

from tests.strategies.var_strats import reg_item_var,reg_item_valid_var,lineage_item_var,lineage_item_valid_var, channel_item_var, channel_item_valid_var
from utils.validators.matrix import reg_item_check,lineage_item_check,channel_item_check

class TestMatrix(unittest.TestCase):

  # TODO: the is a really poorly written test case... Need to rewrite
  @given(st.one_of(reg_item_var(), reg_item_valid_var())) # pylint: disable=no-value-for-parameter
  def test_reg_item_check(self, reg_item):
    # if it does not fit the reg_item dict pattern, return False
    if (array_equal(tuple(reg_item.keys()),reg_keys)):
      expectation = True
    else:
      expectation = False

    result = reg_item_check(reg_item)
    self.assertEqual(result, expectation)
    # if each property does not pass validation, return False
    # if everything else passes, return True

  # TODO: the is a really poorly written test case... Need to rewrite
  @given(st.one_of(lineage_item_var(), lineage_item_valid_var())) # pylint: disable=no-value-for-parameter
  def test_lineage_item_check(self, lineage_item):
    # if it does not fit the lineage_item dict pattern, return False
    expectation = (array_equal(tuple(lineage_item.keys()),lineage_keys))

    result = lineage_item_check(lineage_item)
    self.assertEqual(result, expectation)
    # if each property does not pass validation, return False
    # if everything else passes, return True

  @given(st.one_of(channel_item_var(), channel_item_valid_var())) # pylint: disable=no-value-for-parameter
  def test_channel_item_check(self, channel_item):
    # if it does not fit the channel_item dict pattern, return False
    invalidity = 0
    for i in channel_keys:
      if not i in channel_item:
        invalidity = invalidity + 1

    expectation = invalidity == 0

    result = channel_item_check(channel_item)
    self.assertEqual(result, expectation)
    # if each property does not pass validation, return False
    # if everything else passes, return True
if __name__ == '__main__':
  unittest.main()