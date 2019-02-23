import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packaging_rules.packaging_rule import PackagingRule
from data.axioms.configs import id_pattern
from data.axioms.enums import RuleType

class TestPackagingRule(unittest.TestCase):
  def setUp(self):
    self.rule = PackagingRule(RuleType.CELL, 'A')
  
  @given(st.sampled_from(RuleType),st.from_regex(id_pattern))
  def test_base_rule(self, arb_type, arb_id):
    rule = PackagingRule(arb_type, arb_id)
    self.assertEqual(rule.type, arb_type)
    self.assertEqual(rule.id, arb_id)