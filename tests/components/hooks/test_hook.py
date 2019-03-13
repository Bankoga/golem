import unittest

from hypothesis import given
import hypothesis.strategies as st

from components.hooks.hook import Hook
from components.axioms.props import dest_key_pattern, old_id_pattern 
from components.enums.prop_types import FieldType,HookType,RsrcType,PackType
from components.packages.misc_funcs import build_address, build_meld
from tests.components.packages.test_package import TestPackage
from tests.strategies.packing_strats import arbitrary_id
from tests.strategies.pos_strats import arb_addr,full_address,partial_address
from tests.strategies.prop_strats import package_field_shape,set_type_prop,package_resource,hook_type,package_type

class TestHook(TestPackage):
  # def setUp(self):
    # self.hook = Hook()
  # NO TOUCHY OUTPUTS UNTIL DONE WITH HOOKS!!!!!!
  # @given(st.text(), st.text(), st.text())
  # def test_init(self,hook_id,hook_type, direction, target):
  #   hook = Hook(hook_type, direction, target)
  #   self.assertEqual(hook.hook_type, hook_type)
  #   self.assertEqual(hook.direction, direction)
  #   self.assertEqual(hook.target, target)

  def _build_inputs_meld_(self,hook_id,hook_type, addr,dp_resource,dp_type,dp_shape):
    meld = build_meld(addr,dp_resource,dp_type,dp_shape)
    return f'{hook_id};{hook_type};{meld}'

  def _read_data_(self, meld):
    hook=Hook(meld)
    hook.read_data()
    meld_tuple = meld.split(';')
    self.assertTrue(hook.hook_id == meld_tuple[0])
    if meld_tuple[1]:
      self.assertTrue(hook.hook_type == HookType.UNSET or hook.hook_type==HookType(meld_tuple[1]))
    else:
      self.assertTrue(hook.hook_type == HookType.UNSET)
    self.assertTrue(hook.address==meld_tuple[2])
    if len(meld_tuple)>3 and meld_tuple[3]:
      self.assertTrue(hook.resource == RsrcType.UNSET or hook.resource==RsrcType(meld_tuple[3]))
    else:
      self.assertTrue(hook.resource == RsrcType.UNSET)
    if len(meld_tuple)>4 and meld_tuple[4]:
      self.assertTrue(hook.ctg_type == PackType.UNSET or hook.ctg_type==PackType(meld_tuple[4]))
    else:
      self.assertTrue(hook.ctg_type == PackType.UNSET)
    if len(meld_tuple)>5 and meld_tuple[5]:
      self.assertTrue(hook.shape == FieldType.UNSET or hook.shape==meld_tuple[5])
    else:
      self.assertTrue(hook.shape == FieldType.UNSET)

  def _read_data_alt_(self,hook_id,hook_type,meld):
    hook=Hook(meld,hook_id,hook_type)
    hook.read_data()
    meld_tuple = meld.split(';')
    self.assertTrue(hook.hook_id == hook_id)
    if hook_type:
      self.assertTrue(hook.hook_type == HookType.UNSET or hook.hook_type==HookType(hook_type))
    else:
      self.assertTrue(hook.hook_type == HookType.UNSET)
    self.assertTrue(hook.address==meld_tuple[0])
    if len(meld_tuple)>1 and meld_tuple[1]:
      self.assertTrue(hook.resource == RsrcType.UNSET or hook.resource==RsrcType(meld_tuple[1]))
    else:
      self.assertTrue(hook.resource == RsrcType.UNSET)
    if len(meld_tuple)>2 and meld_tuple[2]:
      self.assertTrue(hook.ctg_type == PackType.UNSET or hook.ctg_type==PackType(meld_tuple[2]))
    else:
      self.assertTrue(hook.ctg_type == PackType.UNSET)
    if len(meld_tuple)>3 and meld_tuple[3]:
      self.assertTrue(hook.shape == FieldType.UNSET or hook.shape==meld_tuple[3])
    else:
      self.assertTrue(hook.shape == FieldType.UNSET)

  def setUp(self):
    # In order to test all the variants for the integration, we will need BDD tests
    self.meld = build_meld('m_id-g_id',RsrcType.ENERGY,PackType.AGGREGATE,FieldType.TEST_INPUT)
    self.hook_id = 'cycle'
    self.hook_type = HookType.UNI
    self.hook=Hook(self.meld,self.hook_id,self.hook_type)

  @given(st.tuples(st.text(),st.text(),st.from_regex(dest_key_pattern),st.text(),st.text(), st.text()))
  def test_read_data(self,meld_tuple):
    meld = ";".join(meld_tuple)
    self._read_data_(meld)

  @given(arbitrary_id(), hook_type(), arb_addr(), package_resource(), package_type(), package_field_shape()) # pylint: disable=no-value-for-parameter
  def test_sampled_msg_read(self,hook_id,hook_type,addr,dp_resource,dp_type,dp_shape):
    inputs = self._build_inputs_meld_(hook_id,hook_type,addr,dp_resource,dp_type,dp_shape)
    self._read_data_(inputs)
    meld = build_meld(addr,dp_resource,dp_type,dp_shape)
    self._read_data_alt_(hook_id,hook_type,meld)

  def _check_hook_(self,container_id):
    if not container_id:#'\n' in container_id or 
      self.assertEqual(self.hook.hook_id, self.hook_id)
    else:
      self.assertEqual(self.hook.hook_id,f'{container_id}-{self.hook_id}')

  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_update_valid_once(self,container_id):
    self.hook=Hook(self.meld,self.hook_id,self.hook_type)
    self.hook.update_id(container_id)
    self._check_hook_(container_id)
  
  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_update_invalidly(self,container_id):
    self.hook=Hook(self.meld,self.hook_id,self.hook_type)
    self.hook.update_id(container_id)
    if container_id:
      for i in range(5):
        self.hook.update_id(f'{container_id}-{i}')
    self._check_hook_(container_id)

if __name__ == '__main__':
    unittest.main()