from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.axioms.pos import cardinal_keys
from components.enums.pos import Floor, CtgType, Dimension
from components.channels.channel import Channel
from components.vars.data import Address
from utils.helpers.props import build_addr_id

from tests.strategies.prop_strats import arbitrary_id

from utils.pos import Pos

@composite
def full_address(draw):
  ids = draw(st.lists(arbitrary_id(),max_size=7)) # pylint: disable=no-value-for-parameter
  res = Address(*ids)
  return res

@composite
def partial_address(draw):
  ids = draw(st.lists(arbitrary_id(),max_size=7)) # pylint: disable=no-value-for-parameter
  res = Address(*ids)
  return res

@composite
def rel_addr(draw):
  ids = draw(st.lists(arbitrary_id(),max_size=7)) # pylint: disable=no-value-for-parameter
  res = build_addr_id(ids)
  return res

@composite
def arb_addr(draw):
  addr = draw(st.one_of(partial_address())) # pylint: disable=no-value-for-parameter
  st.assume(addr)
  return addr

@composite
def valid_floor(draw):
  res = draw(st.sampled_from(Floor))
  st.assume(res)
  return res

@composite
def valid_direction(draw):
  res = draw(st.sampled_from(sorted(cardinal_keys.keys())))
  st.assume(res)
  return res

@composite
def dimension_prop(draw):
  res = draw(st.sampled_from(Dimension))
  st.assume(res)
  return res

@composite
def ctg_prop(draw):
  res = draw(st.sampled_from(CtgType))
  st.assume(res)
  return res
  
@composite
def valid_pos(draw): # pylint: disable=no-value-for-parameter
  s = draw(valid_floor()) # pylint: disable=no-value-for-parameter
  x = draw(st.integers(min_value=0))
  y = draw(st.integers(min_value=0))
  z = draw(st.integers(min_value=0))
  st.assume(s and x and y and z)
  pos = Pos(floor=s,x=x,y=y,z=z)
  return pos