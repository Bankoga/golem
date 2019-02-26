import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.configs import id_pattern
from data.axioms.pos_maps import Floors, ordinal_keys
from utils.datapack import Datapack
from utils.helpers.packer import (build_address, build_datapack,
                                  build_datapack_inputs, build_meld)
from utils.pos import Pos
from tests.strategies.enum_strats import datapack_group,datapack_resource,datapack_shape,datapack_type

@composite
def valid_floor(draw):
  res = draw(st.sampled_from(Floors))
  st.assume(res)
  return res

@composite
def valid_directions(draw):
  res = draw(st.sampled_from(ordinal_keys.keys()))
  st.assume(res)
  return res

@composite
def valid_pos(draw):
  s = draw(valid_floor()) # pylint: disable=no-value-for-parameter
  x = draw(st.integers(min_value=0))
  y = draw(st.integers(min_value=0))
  z = draw(st.integers(min_value=0))
  st.assume(s and x and y and z)
  pos = Pos(s,x,y,z)
  return pos