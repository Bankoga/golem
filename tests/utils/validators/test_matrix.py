import unittest

from hypothesis import given
from hypothesis import strategies as st

from utils.validators.matrix import check_registry_item

class TestMatrix(unittest.TestCase):
  
  def test_check_registry_item(self, reg_item):
    # if it does not fit the reg_item dict pattern, return False
    # if each property does not pass validation, return False
    # if everything else passes, return True
    pass

if __name__ == '__main__':
  unittest.main()