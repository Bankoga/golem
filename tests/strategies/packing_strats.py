import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.enums import FieldType,PackType,RsrcType

from utils.datapack import Datapack
from utils.helpers.packer import build_address, build_meld, build_datapack_inputs, build_datapack

"""
What are the pools of object examples we need to draw from?
- Addresses
- Melds
- Datapacks
- Input Sets
- Output Sets
"""

@composite
def arbitrary_id(draw):
  st.text()

@composite
def full_address(draw):
  m_id = draw(arbitrary_id())
  g_id = draw(arbitrary_id())
  st.assume(m_id != g_id)
  st.assume(m_id)
  st.assume(g_id)
  return f'{m_id}-{g_id}'

@composite
def partial_address(draw):
  return draw(arbitrary_id())

@composite
def sender_and_recipient_pair(draw):
  x = draw(st.text(), min_size=1)
  y = draw(st.text(alphabet=x))
  st.assume(x != y)

@composite
def datapack_resource(draw):
  return st.sampled_from(RsrcType)

@composite
def datapack_type(draw):
  return st.sampled_from(PackType)

@composite
def datapack_shape(draw):
  return st.sampled_from(FieldType)

@composite
def protopack(draw):
  rm_id = st.text()
  rg_id = st.text()
  dp_resource = st.sampled_from(RsrcType)
  dp_type = st.sampled_from(PackType)
  return build_meld(rm_id,rg_id,dp_resource,dp_type,'')

@composite
def datapack(draw):
  rm_id = st.text()
  rg_id = st.text()
  dp_resource = st.sampled_from(RsrcType)
  dp_type = st.sampled_from(PackType)
  dp_shape = st.sampled_from(FieldType)
  return build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)

# @composite
# def matrix_type(draw):
#   pass

@composite
def list_of_inputs_and_input_set(draw):
  pass

# def 

@given(st.sampled_from(['SenderModuleId','self','Self']),
st.sampled_from(['sender_group_id','self','Self', '']),
st.sampled_from(RsrcType),
st.sampled_from(PackType),
st.sampled_from(FieldType),
st.sampled_from(['SenderModuleId','self','Self']),
st.sampled_from(['sender_group_id','self','Self','']))
def test_build_datapack_inputs(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
  inputs = build_datapack_inputs(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
  sender_address = build_address(sm_id,sg_id)
  meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
  res = tuple([meld,sender_address])
  self.assertEqual(inputs, res)

@given(st.sampled_from(['SenderModuleId','self','Self']),
st.sampled_from(['sender_group_id','self','Self', '']),
st.sampled_from(RsrcType),
st.sampled_from(PackType),
st.sampled_from(FieldType),
st.sampled_from(['SenderModuleId','self','Self']),
st.sampled_from(['sender_group_id','self','Self','']))
def test_build_datapack(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
  inputs = build_datapack(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
  sender_address = build_address(sm_id,sg_id)
  meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
  res = Datapack(meld,sender_address)
  self.assertEqual(inputs, res)

@composite
def test_pack(draw,inputs):
  """
  but I need a guaranteed order to some of the inputs don't I?
  Why? Bc agg type datapacks get combined in a spatially oriented way
  Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
  Given that each sender has a position, this can be added to the datapack along with sender address (or in place of?)
  Given that we are sent inputs
  When we prepare to evaluate them
  Then we sort them using a guaranteed sort by pos first!

  Where does this sort live? In utils.helpers.pos_help?

  Specifiying inputs for testing datapacks, and things that rely on them is growing more complex
  At this point, I think it makes the most sense to begin work on a datapack series of custom hypothesis strategies

  aggregate datapacks can't exist or not exist as they please
  they must always exist in the correct order to be processed
  Thus we assume that an order id list or dict has been generated which we can compare against
  """
  # build a
  st.lists(st.builds(build_datapack, st.sampled_from(['SenderModuleId','self','Self']),
      st.sampled_from(['sender_group_id','self','Self', '']),
      st.sampled_from(RsrcType),
      st.sampled_from(PackType),
      st.sampled_from(FieldType),
      st.sampled_from(['SenderModuleId','self','Self']),
      st.sampled_from(['sender_group_id','self','Self',''])))
  pass