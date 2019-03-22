import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.axioms.props import pg_data

from utils.helpers.prop_gen_help import draw, draw_from, roll, roll_for_syllables, produce_syllables
import re

class TestPropGenHelp(unittest.TestCase):

  @given(st.integers(min_value=2, max_value=30))
  def test_draw(self, num_sides):
    res = draw(num_sides)
    self.assertTrue(0 <= res and res < num_sides)

  @given(st.lists(st.integers(min_value=2, max_value=30),min_size=2, max_size=30))
  def test_draw_from(self, drawable):
    res = draw_from(drawable)
    self.assertTrue(res)

  @given(st.integers(min_value=2, max_value=30))
  def test_roll(self, num_sides):
    res = roll(num_sides)
    self.assertTrue(0 < res and res <= num_sides)

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

  # @given()
  # def test_rel_label_gen(self, parent, example_child, prefix, suffix):
  #   result = rel_label_gen(parent, example_child, prefix, suffix)

if __name__ == '__main__':
  unittest.main()