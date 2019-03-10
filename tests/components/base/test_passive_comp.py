import unittest

from hypothesis import given
from hypothesis import strategies as st

# from components.base.passive_comp import PassiveComp
from data.enums.prop_types import CtgType
from tests.components.base.test_static_comp import TestStaticComp

class TestPassiveComp(TestStaticComp):
  def setUp(self):
    self.valid_id = 'TotallyValidId'
    self.valid_ctg = CtgType.FSET
    # self.comp = StaticComp(self.valid_id, self.valid_ctg)

if __name__ == '__main__':
  unittest.main()