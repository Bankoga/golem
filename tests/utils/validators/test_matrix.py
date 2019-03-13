import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.vars.misc import reg_keys

from tests.strategies.var_strats import reg_item_var
from utils.validators.matrix import check_registry_item

class TestMatrix(unittest.TestCase):
  
  @given(reg_item_var()) # pylint: disable=no-value-for-parameter
  def test_check_registry_item(self, reg_item):
    # if it does not fit the reg_item dict pattern, return False
    if (not reg_item.keys() in reg_keys):
      expectation = False
    else:
      expectation = True

    result = check_registry_item(reg_item)
    self.assertEqual(result, expectation)
    # if each property does not pass validation, return False
    # if everything else passes, return True

if __name__ == '__main__':
  unittest.main()