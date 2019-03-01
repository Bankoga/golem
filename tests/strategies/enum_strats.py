import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.props import id_pattern 
from data.enums.prop_types import (FieldType, GroupType, HookType,PackType,
                               RsrcType, RuleType)
from components.packages.package import Package
from utils.helpers.packer import (build_address, build_package,
                                  build_package_inputs, build_meld)


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
def package_group(draw):
  res = draw(st.sampled_from(GroupType))
  st.assume(res)
  st.assume(res != GroupType.UNSET)
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
def ruletype(draw):
  res = draw(st.sampled_from(RuleType))
  st.assume(res)
  st.assume(res != RuleType.UNSET)
  return res
