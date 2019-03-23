import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.axioms.cell_types import CellType
from components.axioms.maps.set import get_ids
from components.axioms.matrix import max_resource_value, min_resource_value
from components.axioms.props import id_pattern, invalid_label_pattern
from components.channels.channel import Channel
from components.enums.prop_types import (ChannelType, FieldType, FuncSetType,
                                         HookType, PackagerType, RsrcType,
                                         RuleType, SuperSet)


@composite
def arbitrary_id(draw):
  res = draw(st.from_regex(id_pattern))
  st.assume(res)
  return res

@composite
def arbitrary_invalid_label(draw):
  res = draw(st.from_regex(invalid_label_pattern))
  st.assume(res)
  return res

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
def channel_resource(draw):
  res = draw(st.sampled_from(RsrcType))
  st.assume(res)
  st.assume(res != RsrcType.UNSET)
  return res

@composite
def superset_prop(draw):
  res = draw(st.sampled_from(SuperSet))
  st.assume(res)
  st.assume(res != SuperSet.UNSET)
  return res

@composite
def set_type_prop(draw):
  res = draw(st.sampled_from(FuncSetType))
  st.assume(res)
  st.assume(res != FuncSetType.UNSET)
  return res

@composite
def ch_type(draw):
  res = draw(st.sampled_from(ChannelType))
  st.assume(res)
  st.assume(res != ChannelType.UNSET)
  return res

@composite
def channel_field_shape(draw):
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
    # fs_type = FuncSetType.SENSOR
    # mismatch between arb actual id and arb actual group type
    # group types need to know if an ID is part of their domain
  # vs = set_ids.values()
  fs_type = draw(superset_prop()) # pylint: disable=no-value-for-parameter
  ids = sorted(get_ids(fs_type))
  g_id = draw(st.sampled_from(ids))
  st.assume(fs_type and g_id)
  return f'{fs_type}-{g_id}'
