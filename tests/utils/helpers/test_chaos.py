import unittest

from hypothesis import given
from hypothesis import strategies as st

from utils.helpers.chaos import  draw, draw_from, roll

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

if __name__ == '__main__':
  unittest.main()