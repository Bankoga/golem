import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.props import id_pattern 
from data.axioms.pos_maps import cardinal_keys
from data.enums.pos import Floor
from components.packages.package import Package
from components.packages.misc_funcs import (build_address, build_package,
                                  build_package_inputs, build_meld)
from utils.pos import Pos
from tests.strategies.prop_strats import package_group,package_resource,package_type
from tests.strategies.packing_strats import valid_shape

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
def valid_pos(draw):
  s = draw(valid_floor()) # pylint: disable=no-value-for-parameter
  x = draw(st.integers(min_value=0))
  y = draw(st.integers(min_value=0))
  z = draw(st.integers(min_value=0))
  st.assume(s and x and y and z)
  pos = Pos(s,x,y,z)
  return pos