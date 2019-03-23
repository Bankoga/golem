import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.prop_types import FieldType,ChannelType,RsrcType

from tests.strategies.data_strats import valid_shape
from tests.strategies.pos_strats import full_address,partial_address,arb_addr
from tests.strategies.prop_strats import channel_field_shape,channel_resource,ch_type, arb_label

from components.channels.channel import Channel
from components.channels.misc_funcs import build_address, build_meld, build_channel_inputs, build_package

class TestMiscFuncs(unittest.TestCase):
  # @given(st.text(),st.text())
  @given(arb_label(), arb_label()) # pylint: disable=no-value-for-parameter
  def test_build_address(self, m_id, g_id):
    addr = build_address(m_id, g_id)
    if g_id is None:
      self.assertEqual(addr, f'{m_id}')
    else:
      self.assertEqual(addr, f'{m_id}-{g_id}')

  @given(ch_type(),channel_resource(),arb_addr(),channel_field_shape()) # pylint: disable=no-value-for-parameter
  def test_build_meld(self, ch_type,dp_resource,recip_addr,dp_shape):
    # addr = build_address(rm_id,rg_id)
    meld = build_meld(ch_type,dp_resource,recip_addr,dp_shape)
    if dp_shape is None:
      self.assertEqual(meld, f'{ch_type};{dp_resource};{recip_addr}')
    else:
      self.assertEqual(meld, f'{ch_type};{dp_resource};{recip_addr};{dp_shape}')
  
  @given(st.sampled_from(ChannelType),
  st.sampled_from(RsrcType),
  arb_addr(), # pylint: disable=no-value-for-parameter
  valid_shape(), # pylint: disable=no-value-for-parameter
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_set_id','self','Self','']))
  # st.one_of(full_address,partial_address),
  # HERE, I only need to test building the inputs for packages with great verbage
  def test_build_channel_inputs(self,ch_type,dp_resource,recip_addr,dp_shape,sm_id,sg_id):
    inputs = build_channel_inputs(ch_type,dp_resource,recip_addr,dp_shape,sm_id,sg_id)
    sender_address = build_address(sm_id,sg_id)
    meld = build_meld(ch_type,dp_resource,recip_addr,dp_shape)
    res = tuple([meld,sender_address])
    self.assertEqual(inputs, res)

  @given(st.sampled_from(ChannelType),
  st.sampled_from(RsrcType),
  arb_addr(), # pylint: disable=no-value-for-parameter
  valid_shape(), # pylint: disable=no-value-for-parameter
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_set_id','self','Self','']))
  # HERE, I only need to test building packages with great verbage using data already supplied
  def test_build_package(self,ch_type,dp_resource,recip_addr,dp_shape,sm_id,sg_id):
    inputs = build_package(ch_type,dp_resource,recip_addr,dp_shape,sm_id,sg_id)
    sender_address = build_address(sm_id,sg_id)
    meld = build_meld(ch_type,dp_resource,recip_addr,dp_shape)
    res = Channel(meld,sender_address)
    self.assertEqual(inputs, res)