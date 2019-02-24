import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.configs import id_pattern
from data.axioms.enums import GroupType

from utils.datapack import Datapack
from utils.helpers.packer import build_address, build_meld, build_datapack_inputs, build_datapack

@composite
def datapack_group(draw):
  res = st.sampled_from(GroupType)
  st.assume(res)
  st.assume(res != GroupType.UNSET)
  return res

# @composite
# def arbitrary_id(draw):
#   res = st.text()#from_regex(id_pattern)
#   st.assume(res)
#   return res