import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.component import Component
from data.enums.pos import ComponentType

class TestComponent(unittest.TestCase):

  @given(st.text(),st.sampled_from(ComponentType))
  def test_base_component(self, component_id, component_type):
    comp = Component(component_id, component_type)
    self.assertIsNone(comp.ctg_type)
    self.assertEqual(comp.itm_id, component_id)
    self.assertEqual(comp.op_lvl, ComponentType(component_type))

  @given(st.text(),st.sampled_from(ComponentType))
  def test_get_id(self, component_id, component_type):
    comp = Component(component_id, component_type)
    self.assertEqual(comp.get_id(), component_id)

if __name__ == '__main__':
  unittest.main()