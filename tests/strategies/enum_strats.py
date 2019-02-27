import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.configs import id_pattern
from data.axioms.enums import (FieldType, GroupType, HookType, PackType,
                               RsrcType, RuleType)
from utils.datapack import Datapack
from utils.helpers.packer import (build_address, build_datapack,
                                  build_datapack_inputs, build_meld)


@composite
def hook_type(draw):
  res = st.sampled_from(HookType)
  st.assume(res)
  st.assume(res != HookType.UNSET)
  return res

@composite
def datapack_resource(draw):
  res = st.sampled_from(RsrcType)
  st.assume(res)
  st.assume(res != RsrcType.UNSET)
  return res

@composite
def datapack_group(draw):
  res = st.sampled_from(GroupType)
  st.assume(res)
  st.assume(res != GroupType.UNSET)
  return res

@composite
def datapack_type(draw):
  res = st.sampled_from(PackType)
  st.assume(res)
  st.assume(res != PackType.UNSET)
  return res

@composite
def datapack_field_shape(draw):
  res = st.sampled_from(FieldType)
  st.assume(res)
  st.assume(res != FieldType.UNSET)
  return res

@composite
def ruletype(draw):
  res = st.sampled_from(RuleType)
  st.assume(res)
  st.assume(res != FieldType.UNSET)
  return res
