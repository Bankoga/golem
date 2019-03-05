import unittest

from hypothesis import given
from hypothesis import strategies as st

from numpy import array_equal

from components.component import Component
from data.enums.pos import ComponentType

from tests.strategies.packing_strats import valid_resource_data

class TestComponent(unittest.TestCase):
  def setUp(self):
    self.valid_c_id = 'TotallyValidId'
    self.valid_c_type = ComponentType.SET
    self.comp = Component(self.valid_c_id, self.valid_c_type)

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

  def test_unbuilt(self):
    self.assertFalse(self.comp.is_built())
    with self.assertRaises(RuntimeError):
      self.comp.operate()

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_build(self, data):
    comp = Component(self.valid_c_id, self.valid_c_type)
    self.assertFalse(comp.is_built())
    comp.build(data)
    self.assertTrue(comp.is_built())
    self.assertTrue(array_equal(comp.var, data))
    comp.operate()

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_update_data(self,new_data):
    self.comp.update(new_data)
    self.assertTrue(array_equal(self.comp.var, new_data))
    self.assertFalse(self.comp.is_built())

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def reset(self, new_data):
    self.comp.update(new_data)
    self.comp.reset()
    self.assertIsNone(self.comp.var)
    self.assertFalse(self.comp.is_built())

if __name__ == '__main__':
  unittest.main()