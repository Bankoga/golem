import unittest

from hypothesis import given
from hypothesis import strategies as st

from numpy import array_equal

from components.vars.misc import reg_keys

from tests.strategies.var_strats import reg_item_var,reg_item_valid_var
from utils.validators.matrix import reg_item_check

class TestMatrix(unittest.TestCase):
  
  @given(st.one_of(reg_item_var(), reg_item_valid_var())) # pylint: disable=no-value-for-parameter
  def test_reg_item_check(self, reg_item):
    # if it does not fit the reg_item dict pattern, return False
    if (array_equal(list(reg_item.keys()),reg_keys)):
      expectation = True
    else:
      expectation = False

    result = reg_item_check(reg_item)
    self.assertEqual(result, expectation)
    # if each property does not pass validation, return False
    # if everything else passes, return True

if __name__ == '__main__':
  unittest.main()