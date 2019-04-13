import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.matrix.lineage_registry import LineageRegistry
from components.base.mechanisms.mechanism import Mechanism
from components.enums.pos import CtgType
from tests.strategies.data_strats import valid_resource_data, valid_resource_array
from components.vars.data import Lineage

from tests.components.base.test_buildable_comp import TestBuildableComp

from tests.strategies.matrix_strats import lineage_reg
from tests.strategies.pos_strats import arb_lineage

class TestMechanism(TestBuildableComp):
  def set_up_base(self):
    self.label = 'pr_0'
    self.ctg = CtgType.PACKAGER
    self.comp_class = Mechanism

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_registry')
    self.lineage = Lineage(golem='a',matrix='l',module='b')
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

  def test_get_registry(self):
    self.assertEqual(self.comp.registry, self.var[0])

  @given(st.one_of(lineage_reg(), st.integers())) # pylint: disable=no-value-for-parameter
  def test_set_registry(self, possible_reg):
    if type(possible_reg) == LineageRegistry:
      self.comp.registry = possible_reg
      self.assertEqual(self.comp.registry, possible_reg)
    else:
      with self.assertRaises(RuntimeError):
        self.comp.registry = possible_reg

  def test_pre_registered_state(self):
    self.assertFalse(self.comp.is_registered)
    with self.assertRaises(RuntimeError):
      self.comp.operate()

  def test_set_lineage_post_registration(self):
    self.comp.register(self.lineage)
    with self.assertRaises(RuntimeError):
      self.comp.lineage = 'Anything'

  @given(arb_lineage()) # pylint: disable=no-value-for-parameter
  def test_set_lineage_pre_registration(self, lineage):
    self.lineage = lineage
    self.assertEqual(self.lineage, lineage)

  def test_set_is_registered(self):
    with self.assertRaises(RuntimeError):
      self.comp.is_registered = True

  def test_reg_item(self):
    self.comp.register(self.lineage)
    self.maxDiff = None
    self.assertEqual(self.comp.reg_item, self.reg_item)
  
  def test_set_reg_item(self):
    with self.assertRaises(RuntimeError):
      self.comp.reg_item = {}

  def test_register(self):
    self.comp.register(self.lineage)
    """
    For every worker, what needs to be registered?
    successful registration means
    - that a registry item has been added to itself
    - that the registry indicated has had the generated reg item added to it
    - that it is ready for operation! (does this mean it is ready to receive packages? yes)
    """
    self.assertTrue(self.comp.is_registered)

  def operate_helper(self, inputs):
    if not self.comp.is_built:
      self.comp.build()
      self.comp.register(self.lineage)
    res = self.comp.operate(*inputs)
    if type(res) is bool:
      self.assertFalse(res)
    else:
      self.assertTrue(not res is False)

  @given(st.one_of(st.lists(st.text()),st.lists(st.integers()),valid_resource_array())) # pylint: disable=no-value-for-parameter
  def test_operate(self, inputs):
    self.operate_helper(inputs)

  @given(st.one_of(st.lists(st.text()),st.lists(st.integers()),valid_resource_array())) # pylint: disable=no-value-for-parameter
  def test_operation_details(self,inputs):
    res = self.comp.operation_details(*inputs)
    if len(inputs)>0:
      self.assertTrue(len(res)>0)
    else:
      self.assertFalse(res)

  def test_build_with_data(self):
    self.comp.build(lineage=self.lineage)
    self.assertEqual(self.comp.var, self.var)
    self.assertTrue(self.comp.is_built)

  # TODO: implement mechanism equality during lineage and mechanism label refactor
  # def test_equality(self):
  #   # Two mechanisms are considered equal if they have the same lineage
  #   # lineages are unique
  #   comp = self.comp_class(*self.values,label=self.label)
  #   self.assertEqual(comp, self.comp)


if __name__ == '__main__':
  unittest.main()