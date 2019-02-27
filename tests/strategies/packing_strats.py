import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.configs import id_pattern
from data.axioms.enums import FieldType, HookType, PackType, RsrcType
from utils.datapack import Datapack
from utils.helpers.packer import (build_address, build_datapack,
                                  build_datapack_inputs, build_meld)
from tests.strategies.enum_strats import datapack_group,datapack_resource,datapack_shape,datapack_type

"""
What are the pools of object examples we need to draw from?
- Addresses
- Melds
- Datapacks
- Input Sets
- Output Sets

TODO: Figure out how to fix pylint errors for hypothesis composite decorator methods
"""

@composite
def arbitrary_id(draw):
  res = st.text()#from_regex(id_pattern)
  st.assume(res)
  return res

@composite
def full_address(draw):
  m_id = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  g_id = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  st.assume(m_id != g_id)
  st.assume(m_id)
  st.assume(g_id)
  return f'{m_id}-{g_id}'

@composite
def partial_address(draw):
  m_id = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  st.assume(m_id)
  return m_id

@composite
def datapack_address(draw):
  addr = st.one_of(full_address(),partial_address()) # pylint: disable=no-value-for-parameter
  st.assume(addr)
  return addr

@composite
def sender_and_recipient_pair(draw):
  recip_addr = datapack_address() # pylint: disable=no-value-for-parameter
  sender_addr = datapack_address() # pylint: disable=no-value-for-parameter
  st.assume(recip_addr != sender_addr)
  st.assume(recip_addr)
  st.assume(sender_addr)
  return (recip_addr, sender_addr)


@composite
def proto_meld(draw):
  addr = draw(datapack_address()) # pylint: disable=no-value-for-parameter
  dp_resource = draw(datapack_resource()) # pylint: disable=no-value-for-parameter
  dp_type = draw(datapack_type()) # pylint: disable=no-value-for-parameter
  meld = build_meld(addr,dp_resource,dp_type)
  return meld

@composite
def full_meld(draw):
  addr = draw(datapack_address()) # pylint: disable=no-value-for-parameter
  dp_resource = draw(datapack_resource()) # pylint: disable=no-value-for-parameter
  dp_type = draw(datapack_type()) # pylint: disable=no-value-for-parameter
  dp_shape = draw(datapack_shape()) # pylint: disable=no-value-for-parameter
  meld = build_meld(addr,dp_resource,dp_type,dp_shape)
  return meld

@composite
def datapack_inputs(draw):
  meld = draw(st.one_of(proto_meld(),full_meld())) # pylint: disable=no-value-for-parameter
  sender_addr = draw(datapack_address()) # pylint: disable=no-value-for-parameter
  return (meld, sender_addr)

@composite
def datapack_arbitrary(draw):
  inputs = draw(datapack_inputs()) # pylint: disable=no-value-for-parameter
  pack = Datapack(inputs[0], inputs[1])
  return pack

@composite
def valid_datapack_arbitrary(draw):
  inputs = draw(datapack_inputs()) # pylint: disable=no-value-for-parameter
  pack = Datapack(inputs[0], inputs[1])
  """
  given that we have a datapack
  when we want check the conv sign
  then we need it to have been built
  """
  pack.build()
  return pack

@composite
def valid_datapack_from_context(draw):
  pass

@composite
def valid_shapes(draw):
  # l = draw(st.integers(min_value=0, max_value=3))
  # shape = []
  # for i in range(l):
  #   x = draw(st.integers(min_value=0))
  #   st.assume(x)
  #   shape.append(x)
  return tuple([4,4,4])

@composite
def valid_cell_instruction(draw):
  directions = "S"
  conv_shapes = ["4x4","8x8,1"]
  instruction = [directions, conv_shapes]
  return instruction