import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packaging_rules.packaging_rule import PackagingRule
from data.axioms.enums import RuleType

class TestPackagingRule(unittest.TestCase):
  def setUp(self):
    self.rule = PackagingRule(RuleType.CELL)
  
  @given(st.sampled_from(RuleType))
  def test_base_rule(self, arb_type):
    rule = PackagingRule(arb_type)
    self.assertEqual(rule.type, arb_type)
    
  
  def test_pack_valid(self, inputs):
    self.rule.pack(inputs)
    pass