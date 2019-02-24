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



# @composite
# def matrix_type(draw):
#   pass

@composite
def list_of_inputs_and_input_set(draw):
  pass

# def 

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(PackType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self','']))
# def test_build_datapack_inputs(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_datapack_inputs(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_address = build_address(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = tuple([meld,sender_address])
#   self.assertEqual(inputs, res)

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(PackType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self','']))
# def test_build_datapack(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_datapack(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_address = build_address(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = Datapack(meld,sender_address)
#   self.assertEqual(inputs, res)

# @composite
# def test_pack(draw,inputs):
#   """
#   but I need a guaranteed order to some of the inputs don't I?
#   Why? Bc agg type datapacks get combined in a spatially oriented way
#   Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
#   Given that each sender has a position, this can be added to the datapack along with sender address (or in place of?)
#   Given that we are sent inputs
#   When we prepare to evaluate them
#   Then we sort them using a guaranteed sort by pos first!

#   Where does this sort live? In utils.helpers.pos_help?

#   Specifiying inputs for testing datapacks, and things that rely on them is growing more complex
#   At this point, I think it makes the most sense to begin work on a datapack series of custom hypothesis strategies

#   aggregate datapacks can't exist or not exist as they please
#   they must always exist in the correct order to be processed
#   Thus we assume that an order id list or dict has been generated which we can compare against
#   """
#   # build a
#   st.lists(st.builds(build_datapack, st.sampled_from(['SenderModuleId','self','Self']),
#       st.sampled_from(['sender_group_id','self','Self', '']),
#       st.sampled_from(RsrcType),
#       st.sampled_from(PackType),
#       st.sampled_from(FieldType),
#       st.sampled_from(['SenderModuleId','self','Self']),
#       st.sampled_from(['sender_group_id','self','Self',''])))
#   pass
