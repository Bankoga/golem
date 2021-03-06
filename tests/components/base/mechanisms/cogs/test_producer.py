import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.mechanisms.cogs.producer import Producer
from components.enums.pos import CtgType
from components.matrix.lineage_registry import LineageRegistry
from components.vars.data import Lineage
from tests.components.base.mechanisms.test_mechanism import TestMechanism


class TestProducer(TestMechanism):
  def set_up_base(self):
    self.label = 'star_0'
    self.ctg = CtgType.PACKAGER
    self.comp_class = Producer

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_registry')
    self.lineage = Lineage(golem='a',matrix='l',module='b',stage='base',group='randos',packager='star_0')
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.values = [self.registry]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = self.comp_class(*self.values,label=self.label, ctg=self.ctg)
    
  # @given(node_type_prop(),st.from_regex(old_label_pattern)) # pylint: disable=no-value-for-parameter
  # def test_base_rule(self, arb_type, arb_label):
  #   rule = Packager(arb_type, arb_label)
  #   self.assertEqual(rule.ctg_type, arb_type)
  #   self.assertEqual(rule.get_id(), arb_label)
  #   self.assertEqual(self.rule.freq_range, prd['freq_range'])
  #   self.assertEqual(self.rule.init_freq, prd['init_freq'])
  #   self.assertEqual(self.rule.pct_of_pod, prd['pct_of_pod'])
  #   self.assertEqual(self.rule.init_threshhold, prd['init_threshhold'])
  #   self.assertEqual(self.rule.activation_function, prd['activation_function'])

if __name__ == '__main__':
  unittest.main()