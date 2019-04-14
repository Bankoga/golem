from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.axioms.props import directions_pattern
from components.axioms.pos import cardinal_keys
from components.enums.pos import Floor, CtgType, Dimension
from components.channels.channel import Channel
from components.vars.data import Lineage
from utils.helpers.props import build_lineage_id

from tests.strategies.prop_strats import arb_label

from utils.pos import Pos

@composite
def full_lineage(draw):
  ids = draw(st.lists(arb_label(),max_size=7)) # pylint: disable=no-value-for-parameter
  res = Lineage(*ids)
  return res

@composite
def partial_lineage(draw):
  ids = draw(st.lists(arb_label(),max_size=7)) # pylint: disable=no-value-for-parameter
  res = Lineage(*ids)
  return res

@composite
def rel_lineage(draw):
  ids = draw(st.lists(arb_label(),max_size=7)) # pylint: disable=no-value-for-parameter
  res = build_lineage_id(ids)
  return res

@composite
def arb_lineage(draw):
  lineage = draw(st.one_of(partial_lineage())) # pylint: disable=no-value-for-parameter
  st.assume(lineage)
  return lineage

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

@composite
def arb_step_directions(draw):
  res = draw(st.from_regex(directions_pattern))
  return res