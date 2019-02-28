import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packagers.packager import Packager
from data.axioms.configs import id_pattern
from data.axioms.packager import defaults as prd
from data.enums.prop_types import RuleType

class TestPackager(unittest.TestCase):
  def setUp(self):
    self.rule = Packager(RuleType.CELL, 'A')
  
  @given(st.sampled_from(RuleType),st.from_regex(id_pattern))
  def test_base_rule(self, arb_type, arb_id):
    rule = Packager(arb_type, arb_id)
    self.assertEqual(rule.type, arb_type)
    self.assertEqual(rule.id, arb_id)
    self.assertEqual(self.rule.freq_range, prd['freq_range'])
    self.assertEqual(self.rule.init_freq, prd['init_freq'])
    self.assertEqual(self.rule.pct_of_pod, prd['pct_of_pod'])
    self.assertEqual(self.rule.init_threshhold, prd['init_threshhold'])
    self.assertEqual(self.rule.activation_function, prd['activation_function'])