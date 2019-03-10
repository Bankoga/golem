from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.pos_maps import cardinal_keys
from data.enums.pos import Floor, CtgType, Dimension
from components.packages.package import Package
from utils.pos import Pos

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