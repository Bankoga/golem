import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.component import Component

class TestComponent(unittest.TestCase):

  @given(st.text(),st.integers())
  def test_base_component(self, component_id, component_type):
    comp = Component(component_id, component_type)
    self.assertIsNone(comp.id)
    self.assertEqual(comp.c_id, component_id)
    self.assertEqual(comp.c_type, component_type)


if __name__ == '__main__':
  unittest.main()