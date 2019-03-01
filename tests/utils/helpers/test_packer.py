import unittest

from hypothesis import given
from hypothesis import strategies as st

from data.enums.prop_types import FieldType,PackType,RsrcType

from tests.strategies.packing_strats import arbitrary_id,full_address,partial_address,package_address
from tests.strategies.enum_strats import package_field_shape,package_resource,package_type

from components.packages.package import Package
from utils.helpers.packer import build_address, build_meld, build_package_inputs, build_package

class TestPacker(unittest.TestCase):
  # @given(st.text(),st.text())
  @given(arbitrary_id(), arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_build_address(self, m_id, g_id):
    addr = build_address(m_id, g_id)
    if g_id is None:
      self.assertEqual(addr, f'{m_id}')
    else:
      self.assertEqual(addr, f'{m_id}-{g_id}')

  @given(package_address(),package_resource(),package_type(),package_field_shape()) # pylint: disable=no-value-for-parameter
  def test_build_meld(self, recip_addr,dp_resource,dp_type,dp_shape):
    # addr = build_address(rm_id,rg_id)
    meld = build_meld(recip_addr,dp_resource,dp_type,dp_shape)
    if dp_shape is None:
      self.assertEqual(meld, f'{recip_addr};{dp_resource};{dp_type}')
    else:
      self.assertEqual(meld, f'{recip_addr};{dp_resource};{dp_type};{dp_shape}')
  
  @given(package_address(), # pylint: disable=no-value-for-parameter
  st.sampled_from(RsrcType),
  st.sampled_from(PackType),
  st.sampled_from(FieldType),
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_group_id','self','Self','']))
  # st.one_of(full_address,partial_address),
  # HERE, I only need to test building the inputs for packages with great verbage
  def test_build_package_inputs(self,recip_addr,dp_resource,dp_type,dp_shape,sm_id,sg_id):
    inputs = build_package_inputs(recip_addr,dp_resource,dp_type,dp_shape,sm_id,sg_id)
    sender_address = build_address(sm_id,sg_id)
    meld = build_meld(recip_addr,dp_resource,dp_type,dp_shape)
    res = tuple([meld,sender_address])
    self.assertEqual(inputs, res)

  @given(package_address(), # pylint: disable=no-value-for-parameter
  st.sampled_from(RsrcType),
  st.sampled_from(PackType),
  st.sampled_from(FieldType),
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_group_id','self','Self','']))
  # HERE, I only need to test building packages with great verbage using data already supplied
  def test_build_package(self,recip_addr,dp_resource,dp_type,dp_shape,sm_id,sg_id):
    inputs = build_package(recip_addr,dp_resource,dp_type,dp_shape,sm_id,sg_id)
    sender_address = build_address(sm_id,sg_id)
    meld = build_meld(recip_addr,dp_resource,dp_type,dp_shape)
    res = Package(meld,sender_address)
    self.assertEqual(inputs, res)