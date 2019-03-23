import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packagers.packager import Packager
from components.axioms.props import old_label_pattern 
from components.axioms.packager import defaults as prd
from components.enums.prop_types import PackagerType

from tests.strategies.prop_strats import node_type_prop

class TestPackager(unittest.TestCase):
  def setUp(self):
    self.rule = Packager(PackagerType.CELL, 'A')
  
  @given(node_type_prop(),st.from_regex(old_label_pattern)) # pylint: disable=no-value-for-parameter
  def test_base_rule(self, arb_type, arb_label):
    rule = Packager(arb_type, arb_label)
    self.assertEqual(rule.ctg_type, arb_type)
    self.assertEqual(rule.get_id(), arb_label)
    self.assertEqual(self.rule.freq_range, prd['freq_range'])
    self.assertEqual(self.rule.init_freq, prd['init_freq'])
    self.assertEqual(self.rule.pct_of_pod, prd['pct_of_pod'])
    self.assertEqual(self.rule.init_threshhold, prd['init_threshhold'])
    self.assertEqual(self.rule.activation_function, prd['activation_function'])