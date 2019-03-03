import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from data.axioms.cell_types import CellType
from data.axioms.matrix import max_resource_value, min_resource_value
from data.axioms.props import id_pattern
from data.enums.prop_types import SetType, FieldType, HookType, PackType, RsrcType, PackagerType, RuleType
from data.maps.set import get_ids

from components.packages.package import Package
from components.packages.misc_funcs import (build_address, build_package,
                                  build_package_inputs, build_meld)

@composite
def cell_type_prop(draw):
  res = draw(st.sampled_from(CellType))
  st.assume(res)
  st.assume(res != CellType.UNSET)
  return res

@composite
def node_type_prop(draw):
  res = draw(st.sampled_from(PackagerType))
  st.assume(res)
  st.assume(res != PackagerType.UNSET)
  return res


@composite
def hook_type(draw):
  res = draw(st.sampled_from(HookType))
  st.assume(res)
  st.assume(res != HookType.UNSET)
  return res

@composite
def package_resource(draw):
  res = draw(st.sampled_from(RsrcType))
  st.assume(res)
  st.assume(res != RsrcType.UNSET)
  return res

@composite
def set_type_prop(draw):
  res = draw(st.sampled_from(SetType))
  st.assume(res)
  st.assume(res != SetType.UNSET)
  return res

@composite
def package_type(draw):
  res = draw(st.sampled_from(PackType))
  st.assume(res)
  st.assume(res != PackType.UNSET)
  return res

@composite
def package_field_shape(draw):
  res = draw(st.sampled_from(FieldType))
  st.assume(res)
  st.assume(res != FieldType.UNSET)
  return res

@composite
def rule_type_prop(draw):
  res = draw(st.sampled_from(RuleType))
  st.assume(res)
  st.assume(res != RuleType.UNSET)
  return res


@composite
def fs_provider_id(draw):
    # fs_id = set_ids['glg']
    # fs_type = SetType.SENSOR
    # mismatch between arb actual id and arb actual group type
    # group types need to know if an ID is part of their domain
  # vs = set_ids.values()
  g_type = draw(set_type_prop()) # pylint: disable=no-value-for-parameter
  g_id = draw(st.sampled_from(sorted(get_ids(g_type))))
  st.assume(g_type and g_id)
  return f'{g_type}-{g_id}'