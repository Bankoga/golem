import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.prop_types import FieldType,ChannelType,ResourceType

from tests.strategies.data_strats import valid_shape
from tests.strategies.pos_strats import full_lineage,partial_lineage,arb_lineage
from tests.strategies.prop_strats import channel_field_shape,arb_resource_type,arb_channel_type, arb_label

from components.channels.channel import Channel
from components.channels.misc_funcs import build_lineage, build_meld, build_channel_inputs, build_package

class TestMiscFuncs(unittest.TestCase):
  # @given(st.text(),st.text())
  @given(arb_label(), arb_label()) # pylint: disable=no-value-for-parameter
  def test_build_lineage(self, m_id, g_id):
    lineage = build_lineage(m_id, g_id)
    if g_id is None:
      self.assertEqual(lineage, f'{m_id}')
    else:
      self.assertEqual(lineage, f'{m_id}-{g_id}')

  @given(arb_channel_type(),arb_resource_type(),arb_lineage(),channel_field_shape()) # pylint: disable=no-value-for-parameter
  def test_build_meld(self, ch_type,dp_resource,recip_lineage,dp_shape):
    # lineage = build_lineage(rm_id,rg_id)
    meld = build_meld(ch_type,dp_resource,recip_lineage,dp_shape)
    if dp_shape is None:
      self.assertEqual(meld, f'{ch_type};{dp_resource};{recip_lineage}')
    else:
      self.assertEqual(meld, f'{ch_type};{dp_resource};{recip_lineage};{dp_shape}')
  
  @given(st.sampled_from(ChannelType),
  st.sampled_from(ResourceType),
  arb_lineage(), # pylint: disable=no-value-for-parameter
  valid_shape(), # pylint: disable=no-value-for-parameter
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_set_id','self','Self','']))
  # st.one_of(full_lineage,partial_lineage),
  # HERE, I only need to test building the inputs for packages with great verbage
  def test_build_channel_inputs(self,ch_type,dp_resource,recip_lineage,dp_shape,sm_id,sg_id):
    inputs = build_channel_inputs(ch_type,dp_resource,recip_lineage,dp_shape,sm_id,sg_id)
    sender_lineage = build_lineage(sm_id,sg_id)
    meld = build_meld(ch_type,dp_resource,recip_lineage,dp_shape)
    res = tuple([meld,sender_lineage])
    self.assertEqual(inputs, res)

  @given(st.sampled_from(ChannelType),
  st.sampled_from(ResourceType),
  arb_lineage(), # pylint: disable=no-value-for-parameter
  valid_shape(), # pylint: disable=no-value-for-parameter
  st.sampled_from(['SenderModuleId','self','Self']),
  st.sampled_from(['sender_set_id','self','Self','']))
  # HERE, I only need to test building packages with great verbage using data already supplied
  def test_build_package(self,ch_type,dp_resource,recip_lineage,dp_shape,sm_id,sg_id):
    inputs = build_package(ch_type,dp_resource,recip_lineage,dp_shape,sm_id,sg_id)
    sender_lineage = build_lineage(sm_id,sg_id)
    meld = build_meld(ch_type,dp_resource,recip_lineage,dp_shape)
    res = Channel(meld,sender_lineage)
    self.assertEqual(inputs, res)