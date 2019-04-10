from hypothesis import strategies as st
from hypothesis.strategies import composite
from hypothesis import settings
from hypothesis import HealthCheck

from components.axioms.configs import proc_ids,set_ids,set_ids
from components.enums.prop_types import ChannelType,SuperSet

from tests.strategies.prop_strats import set_type_prop
from tests.strategies.channel_strats import channel_arbitrary
from tests.strategies.pos_strats import arb_lineage, partial_lineage
from tests.strategies.data_strats import valid_resource_data

from components.channels.channel import Channel
from components.channels.misc_funcs import build_lineage, build_meld, build_channel_inputs, build_package

from components.mediators.module_builder import fs_services

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
  proc = fs_services.get(proc_ids[proc_id], **{})
  return proc

@composite
def unbuilt_module_input_set(draw):
  return []

@composite
def group_input_set(draw, elements=partial_lineage()): # pylint: disable=no-value-for-parameter
  # the inputs to a module, consist of a bunch of inputs to it and its proc groups
  # thus we need to generate two or more sets of inputs that get merged into one
  # inputs to the module
  lineage = draw(elements)#partial_lineage()) # pylint: disable=no-value-for-parameter
  st.assume(lineage)
  groups = []
  group_inputs = []
  module = draw(proc_group()) # pylint: disable=no-value-for-parameter
  for group in module.groups:
    inp = draw(channel_arbitrary()) # pylint: disable=no-value-for-parameter
    groups.append(module.groups[group]['id'])
    inp.update(f'{lineage}-{module.groups[group]["id"]}')
    resc_data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
    inp.build(resc_data)
    # meld = inp.get_meld()
    group_inputs.append(inp)
  st.assume(group_inputs)
  return group_inputs

# @settings(suppress_health_check=[HealthCheck.filter_too_much])
@composite
def module_input_set(draw, elements=partial_lineage()): # pylint: disable=no-value-for-parameter
  # the inputs to a module, consist of a bunch of inputs to it and its proc groups
  # thus we need to generate two or more sets of inputs that get merged into one
  # inputs to the module
  lineage = draw(elements)#partial_lineage()) # pylint: disable=no-value-for-parameter
  packs_overlay = draw(st.lists(channel_arbitrary(), max_size=3)) # pylint: disable=no-value-for-parameter
  packs_aggrg = draw(st.lists(channel_arbitrary(),max_size=4)) # pylint: disable=no-value-for-parameter
  st.assume(lineage)
  inputs = []
  for pack in packs_overlay:
    pack.update(lineage)
    pack.ctg_type = ChannelType.OVERLAY
    resc_data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
    pack.build(resc_data)
    inputs.append(pack)
  for pack in packs_aggrg:
    pack.update(lineage)
    pack.ctg_type = ChannelType.AGGREGATE
    resc_data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
    pack.build(resc_data)
    inputs.append(pack)
  st.assume(inputs)
  return inputs

@composite
def processed_module_input_set(draw, elements=st.sampled_from(sorted(proc_ids.values()))):
  # Draw a proc id (until all listed func set ids have this implemented)
  fs_id = draw(elements)
  st.assume(fs_id)
  # Draw an input set for the drawn proc id
  inputs = draw(module_input_set(st.just(fs_id))) # pylint: disable=no-value-for-parameter
  # Draw a copy of the proc from proc_service
  fs = fs_services.get(f'{SuperSet.PROC}-{fs_id}')
  st.assume(fs)
  # build the proc
  fs.build()
  # use the proc to process the inputs
  fs_inputs = fs.process_inputs(inputs)
  return (fs_inputs, fs)

@composite
def valid_module_input_set(draw):
  pass

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(ChannelType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self','']))
# def test_build_channel_inputs(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_channel_inputs(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_lineage = build_lineage(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = tuple([meld,sender_lineage])
#   self.assertEqual(inputs, res)

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(ChannelType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self','']))
# def test_build_package(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_package(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_lineage = build_lineage(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = Channel(meld,sender_lineage)
#   self.assertEqual(inputs, res)

# @composite
# def test_pack(draw,inputs):
#   """
#   but I need a guaranteed order to some of the inputs don't I?
#   Why? Bc agg type packages get combined in a spatially oriented way
#   Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
#   Given that each sender has a position, this can be added to the package along with sender lineage (or in place of?)
#   Given that we are sent inputs
#   When we prepare to evaluate them
#   Then we sort them using a guaranteed sort by pos first!

#   Where does this sort live? In utils.helpers.pos_help?

#   Specifiying inputs for testing packages, and things that rely on them is growing more complex
#   At this point, I think it makes the most sense to begin work on a package series of custom hypothesis strategies

#   aggregate packages can't exist or not exist as they please
#   they must always exist in the correct order to be processed
#   Thus we assume that an order id list or dict has been generated which we can compare against
#   """
#   # build a
#   st.lists(st.builds(build_package, st.sampled_from(['SenderModuleId','self','Self']),
#       st.sampled_from(['sender_set_id','self','Self', '']),
#       st.sampled_from(RsrcType),
#       st.sampled_from(ChannelType),
#       st.sampled_from(FieldType),
#       st.sampled_from(['SenderModuleId','self','Self']),
#       st.sampled_from(['sender_set_id','self','Self',''])))
#   pass
