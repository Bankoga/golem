import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from components.axioms.props import id_pattern
from tests.strategies.prop_strats import (package_field_shape, package_resource, package_type)
from tests.strategies.data_strats import valid_resource_data
from components.packages.package import Package
from components.packages.misc_funcs import (build_meld)

"""
What are the pools of object examples we need to draw from?
- Addresses
- Melds
- Packages
- Input Sets
- Output Sets
"""

@composite
def arbitrary_id(draw):
  res = draw(st.from_regex(id_pattern))
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
def package_address(draw):
  addr = st.one_of(full_address(),partial_address()) # pylint: disable=no-value-for-parameter
  st.assume(addr)
  return addr

@composite
def sender_and_recipient_pair(draw):
  recip_addr = package_address() # pylint: disable=no-value-for-parameter
  sender_addr = package_address() # pylint: disable=no-value-for-parameter
  st.assume(recip_addr != sender_addr)
  st.assume(recip_addr)
  st.assume(sender_addr)
  return (recip_addr, sender_addr)


@composite
def proto_meld(draw):
  addr = draw(package_address()) # pylint: disable=no-value-for-parameter
  dp_resource = draw(package_resource()) # pylint: disable=no-value-for-parameter
  dp_type = draw(package_type()) # pylint: disable=no-value-for-parameter
  meld = build_meld(addr,dp_resource,dp_type)
  return meld

@composite
def full_meld(draw):
  addr = draw(package_address()) # pylint: disable=no-value-for-parameter
  dp_resource = draw(package_resource()) # pylint: disable=no-value-for-parameter
  dp_type = draw(package_type()) # pylint: disable=no-value-for-parameter
  dp_shape = draw(package_field_shape()) # pylint: disable=no-value-for-parameter
  meld = build_meld(addr,dp_resource,dp_type,dp_shape)
  return meld

@composite
def package_inputs(draw):
  meld = draw(st.one_of(proto_meld(),full_meld())) # pylint: disable=no-value-for-parameter
  sender_addr = draw(package_address()) # pylint: disable=no-value-for-parameter
  return (meld, sender_addr)

@composite
def valid_cell_instruction(draw):
  directions = "S"
  conv_shapes = ["4x4","8x8,1"]
  instruction = [directions, conv_shapes]
  return instruction

@composite
def package_arbitrary(draw):
  inputs = draw(package_inputs()) # pylint: disable=no-value-for-parameter
  pack = Package(inputs[0], inputs[1])
  return pack

@composite
def valid_package_arbitrary(draw):
  inputs = draw(package_inputs()) # pylint: disable=no-value-for-parameter
  pack = Package(inputs[0], inputs[1])
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
#   pack = draw(package_arbitrary()): # pylint: disable=no-value-for-parameter
#   pack.build()
#   return pack

@composite
def valid_package_from_context(draw):
  pass
