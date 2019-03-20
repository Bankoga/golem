import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from components.axioms.props import id_pattern
from components.channels.channel import Channel
from components.channels.misc_funcs import (build_meld)

from tests.strategies.pos_strats import full_address, partial_address, arb_addr
from tests.strategies.prop_strats import (channel_field_shape, channel_resource, channel_type)
from tests.strategies.data_strats import valid_resource_data

"""
What are the pools of object examples we need to draw from?
- Melds
- Packages
- Input Sets
- Output Sets
"""

@composite
def sender_and_recipient_pair(draw):
  recip_addr = arb_addr() # pylint: disable=no-value-for-parameter
  sender_addr = arb_addr() # pylint: disable=no-value-for-parameter
  st.assume(recip_addr != sender_addr)
  st.assume(recip_addr)
  st.assume(sender_addr)
  return (recip_addr, sender_addr)


@composite
def proto_meld(draw):
  addr = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  dp_resource = draw(channel_resource()) # pylint: disable=no-value-for-parameter
  dp_type = draw(channel_type()) # pylint: disable=no-value-for-parameter
  meld = build_meld(addr,dp_resource,dp_type)
  return meld

@composite
def full_meld(draw):
  addr = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  dp_resource = draw(channel_resource()) # pylint: disable=no-value-for-parameter
  dp_type = draw(channel_type()) # pylint: disable=no-value-for-parameter
  dp_shape = draw(channel_field_shape()) # pylint: disable=no-value-for-parameter
  meld = build_meld(addr,dp_resource,dp_type,dp_shape)
  return meld

@composite
def channel_inputs(draw):
  meld = draw(st.one_of(proto_meld(),full_meld())) # pylint: disable=no-value-for-parameter
  sender_addr = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  return (meld, sender_addr)

@composite
def valid_cell_instruction(draw):
  directions = "S"
  conv_shapes = ["4x4","8x8,1"]
  instruction = [directions, conv_shapes]
  return instruction

@composite
def channel_arbitrary(draw):
  inputs = draw(channel_inputs()) # pylint: disable=no-value-for-parameter
  pack = Channel(inputs[0], inputs[1])
  return pack

@composite
def valid_channel_arbitrary(draw):
  inputs = draw(channel_inputs()) # pylint: disable=no-value-for-parameter
  pack = Channel(inputs[0], inputs[1])
  """
  given that we have a package
  when we want check the conv sign
  then we need it to have been built
  """
  resc_data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
  pack.build(resc_data)
  st.assume(pack and resc_data.any())
  return pack


# @composite
# def input_pack_arbitrary(draw):
#   pack = draw(channel_arbitrary()): # pylint: disable=no-value-for-parameter
#   pack.build()
#   return pack

@composite
def valid_channel_from_context(draw):
  pass
