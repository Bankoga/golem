import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from data.axioms.matrix import max_resource_value, min_resource_value
from data.axioms.props import id_pattern
from data.enums.prop_types import FieldType, HookType, PackType, RsrcType, NodeType
from data.axioms.cell_types import CellType
from tests.strategies.enum_strats import (package_field_shape, package_group,
                                          package_resource, package_type)
from components.packages.package import Package
from utils.helpers.packer import (build_address, build_package,
                                  build_package_inputs, build_meld)

@composite
def cell_type_prop(draw):
  res = draw(st.sampled_from(CellType))
  st.assume(res)
  st.assume(res != CellType.UNSET)
  return res

@composite
def node_type_prop(draw):
  res = draw(st.sampled_from(NodeType))
  st.assume(res)
  st.assume(res != NodeType.UNSET)
  return res