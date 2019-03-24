import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.weighted_comp import WeightedComp
from components.enums.pos import CtgType

from tests.components.base.test_static_comp import TestStaticComp

class TestWeightedComp(TestStaticComp):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.INSTRUCTION
  
  def setUp(self):
    self.set_up_base()
    self.comp = WeightedComp(label=self.label, ctg=self.ctg)

if __name__ == '__main__':
  unittest.main()