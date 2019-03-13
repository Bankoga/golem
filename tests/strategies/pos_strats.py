from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.axioms.pos import cardinal_keys
from components.enums.pos import Floor, CtgType, Dimension
from components.packages.package import Package

from tests.strategies.prop_strats import arbitrary_id

from utils.pos import Pos

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
def arb_addr(draw):
  addr = st.one_of(full_address(),partial_address()) # pylint: disable=no-value-for-parameter
  st.assume(addr)
  return addr

@composite
def valid_floor(draw):
  res = draw(st.sampled_from(Floor))
  st.assume(res)
  return res

@composite
def valid_locale(draw):
  res = {}
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
def valid_pos(draw, elements=ctg_prop()): # pylint: disable=no-value-for-parameter
  comp_type = draw(elements)
  s = draw(valid_floor()) # pylint: disable=no-value-for-parameter
  x = draw(st.integers(min_value=0))
  y = draw(st.integers(min_value=0))
  z = draw(st.integers(min_value=0))
  st.assume(comp_type and s and x and y and z)
  pos = Pos(comp_type,s,x,y,z)
  return pos