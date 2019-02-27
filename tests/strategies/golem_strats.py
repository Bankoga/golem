import unittest

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import composite

from data.axioms.configs import id_pattern
from data.axioms.enums import GroupType

from tests.strategies.packing_strats import datapack_arbitrary,valid_datapack_arbitrary, datapack_address, partial_address

from utils.datapack import Datapack
from utils.helpers.packer import build_address, build_meld, build_datapack_inputs, build_datapack

from data.axioms.configs import proc_ids
from components.procs.proc_provider import proc_services

@composite
def list_of_inputs_and_input_set(draw):
  # pylint: disable=no-value-for-parameter
  pass

@composite
def valid_input_output_pair(draw):
  pass


@composite
def proc_group(draw):
  proc_id = draw(st.sampled_from(sorted(proc_ids.keys())))
  proc = proc_services.get(proc_ids[proc_id], **{})
  return proc

@composite
def module_input_set(draw):
  # the inputs to a module, consist of a bunch of inputs to it and its proc groups
  # thus we need to generate two or more sets of inputs that get merged into one
  # inputs to the module
  address = draw(partial_address()) # pylint: disable=no-value-for-parameter
  packs = draw(st.lists(datapack_arbitrary())) # pylint: disable=no-value-for-parameter
  st.assume(address and packs)
  inputs = {}
  for pack in packs:
    pack.update(address)
    pack.build()
    meld = pack.get_meld()
    inputs[meld] = pack
  # inputs to the hooks
  groups = []
  group_inputs = {}
  funcgroup = draw(proc_group()) # pylint: disable=no-value-for-parameter
  for group in funcgroup.groups:
    inp = draw(datapack_arbitrary()) # pylint: disable=no-value-for-parameter
    groups.append(funcgroup.groups[group]['id'])
    inp.update(f'{address}-{funcgroup.groups[group]["id"]}')
    inp.build()
    meld = inp.get_meld()
    group_inputs[meld] = inp
  # inputs to the specific groups
  st.assume(inputs)
  return inputs

@composite
def processed_module_input_set(draw):
  base_set = draw(module_input_set()) # pylint: disable=no-value-for-parameter
  processing a module input set consists of a few parts
    - removing aggregate datapacks from the inputs
    - combining them in a guaranteed order
    - then readding a single entry per aggregated key
    

  return base_set

@composite
def valid_module_input_set(draw):
  pass

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(PackType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self','']))
# def test_build_datapack_inputs(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_datapack_inputs(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_address = build_address(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = tuple([meld,sender_address])
#   self.assertEqual(inputs, res)

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(PackType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_group_id','self','Self','']))
# def test_build_datapack(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_datapack(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_address = build_address(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = Datapack(meld,sender_address)
#   self.assertEqual(inputs, res)

# @composite
# def test_pack(draw,inputs):
#   """
#   but I need a guaranteed order to some of the inputs don't I?
#   Why? Bc agg type datapacks get combined in a spatially oriented way
#   Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
#   Given that each sender has a position, this can be added to the datapack along with sender address (or in place of?)
#   Given that we are sent inputs
#   When we prepare to evaluate them
#   Then we sort them using a guaranteed sort by pos first!

#   Where does this sort live? In utils.helpers.pos_help?

#   Specifiying inputs for testing datapacks, and things that rely on them is growing more complex
#   At this point, I think it makes the most sense to begin work on a datapack series of custom hypothesis strategies

#   aggregate datapacks can't exist or not exist as they please
#   they must always exist in the correct order to be processed
#   Thus we assume that an order id list or dict has been generated which we can compare against
#   """
#   # build a
#   st.lists(st.builds(build_datapack, st.sampled_from(['SenderModuleId','self','Self']),
#       st.sampled_from(['sender_group_id','self','Self', '']),
#       st.sampled_from(RsrcType),
#       st.sampled_from(PackType),
#       st.sampled_from(FieldType),
#       st.sampled_from(['SenderModuleId','self','Self']),
#       st.sampled_from(['sender_group_id','self','Self',''])))
#   pass
