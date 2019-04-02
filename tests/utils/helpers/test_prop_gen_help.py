import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.axioms.props import pg_data
from tests.strategies.prop_strats import arb_label
from utils.helpers.prop_gen_help import roll_for_syllables, produce_syllables, roll_name, kin_label_gen_unique, roll_new_name
from utils.validators.prop_validators import is_valid_label
import re

class TestPropGenHelp(unittest.TestCase):

  @given(st.integers(min_value=1, max_value=30))
  def test_produce_syllables(self,num_syllables):
    res = produce_syllables(num_syllables)
    self.assertEqual(len(res),num_syllables)
    for i in res:
      match = re.match(pg_data['vowel_pattern'], i)
      self.assertTrue(i in pg_data['syllables'] or (not match is None and len(match)==1))

  def test_roll_for_syllables(self):
    res = roll_for_syllables()
    l = len(res)
    self.assertTrue(0 < l and l <= pg_data['max_syllables'])
    for i in res:
      match = re.match(pg_data['vowel_pattern'], i)
      self.assertTrue(i in pg_data['syllables'] or (not match is None and len(match)==1))

  def test_roll_name(self):
    res = roll_name()
    self.assertTrue(is_valid_label(res))

  def test_roll_new_name(self):
    old_names = []
    for i in range(20):
      old_names.append(roll_name())
    res = roll_new_name(old_names)
    self.assertTrue(is_valid_label(res))

  @given(arb_label(), st.integers(max_value=1000), st.text(), st.text()) # pylint: disable=no-value-for-parameter
  def test_kin_label_gen_unique(self, parent, num_children, prefix, suffix):
    results = kin_label_gen_unique(parent, num_children, prefix, suffix)
    for res in results:
      self.assertTrue(is_valid_label(res))

if __name__ == '__main__':
  unittest.main()