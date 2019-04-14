import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.axioms.props import name_gen_data
from tests.strategies.prop_strats import arb_label
from utils.helpers.namerinator import roll_for_syllables, produce_syllables, roll_name, kin_label_gen_unique, roll_new_name, get_sound_type_of_char, produce_arb_syllable
from utils.validators.prop_validators import is_valid_label
import re

class TestNamerinator(unittest.TestCase):

  @given(st.characters())
  def test_get_sound_type_of_char(self, character):
    res = get_sound_type_of_char(character)
    if character in name_gen_data['vowels']:
      self.assertEqual(res, 'vowel')
    elif character in name_gen_data['consonants']:
      self.assertEqual(res, 'consonant')
    else:
      self.assertEqual(res, 'unrecognized')

  def test_produce_arb_syllable(self):
    res = produce_arb_syllable()
    prev_chars = []
    for i,char in enumerate(res):
      # act based on state_of_prev_char and current char
      last_type = get_sound_type_of_char(prev_chars[i-1])
      prev_chars.append(char)

  @given(st.integers(min_value=1, max_value=30))
  def test_produce_syllables(self,num_syllables):
    res = produce_syllables(num_syllables)
    self.assertEqual(len(res),num_syllables)
    for i in res:
      match = re.match(name_gen_data['vowel_pattern'], i)
      self.assertTrue(i in name_gen_data['syllables'] or (not match is None and len(match)==1))

  def test_roll_for_syllables(self):
    res = roll_for_syllables()
    l = len(res)
    self.assertTrue(0 < l and l <= name_gen_data['max_syllables'])
    for i in res:
      match = re.match(name_gen_data['vowel_pattern'], i)
      self.assertTrue(i in name_gen_data['syllables'] or (not match is None and len(match)==1))

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