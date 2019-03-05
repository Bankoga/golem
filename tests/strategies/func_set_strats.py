from hypothesis import strategies as st
from hypothesis.strategies import composite
from hypothesis import settings
from hypothesis import HealthCheck

from data.axioms.configs import proc_ids,set_ids
from data.enums.prop_types import PackType

from tests.strategies.prop_strats import set_type_prop
from tests.strategies.packing_strats import package_arbitrary, package_address, partial_address,valid_resource_data

from components.packages.package import Package
from components.packages.misc_funcs import build_address, build_meld, build_package_inputs, build_package

from components.func_sets.procs.proc_provider import proc_services

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
def unbuilt_module_input_set(draw):
  return []

@composite
def group_input_set(draw, elements=partial_address()): # pylint: disable=no-value-for-parameter
  # the inputs to a module, consist of a bunch of inputs to it and its proc groups
  # thus we need to generate two or more sets of inputs that get merged into one
  # inputs to the module
  address = draw(elements)#partial_address()) # pylint: disable=no-value-for-parameter
  st.assume(address)
  groups = []
  group_inputs = []
  funcset = draw(proc_group()) # pylint: disable=no-value-for-parameter
  for group in funcset.groups:
    inp = draw(package_arbitrary()) # pylint: disable=no-value-for-parameter
    groups.append(funcset.groups[group]['id'])
    inp.update(f'{address}-{funcset.groups[group]["id"]}')
    resc_data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
    inp.build(resc_data)
    meld = inp.get_meld()
    group_inputs.append(inp)
  st.assume(group_inputs)
  return group_inputs

# @settings(suppress_health_check=[HealthCheck.filter_too_much])
@composite
def module_input_set(draw, elements=partial_address()): # pylint: disable=no-value-for-parameter
  # the inputs to a module, consist of a bunch of inputs to it and its proc groups
  # thus we need to generate two or more sets of inputs that get merged into one
  # inputs to the module
  address = draw(elements)#partial_address()) # pylint: disable=no-value-for-parameter
  packs_overlay = draw(st.lists(package_arbitrary(), max_size=3)) # pylint: disable=no-value-for-parameter
  packs_aggrg = draw(st.lists(package_arbitrary(),max_size=4)) # pylint: disable=no-value-for-parameter
  st.assume(address)
  inputs = []
  for pack in packs_overlay:
    pack.update(address)
    pack.ctg_type = PackType.OVERLAY
    resc_data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
    pack.build(resc_data)
    inputs.append(pack)
  for pack in packs_aggrg:
    pack.update(address)
    pack.ctg_type = PackType.AGGREGATE
    resc_data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
    pack.build(resc_data)
    inputs.append(pack)
  st.assume(inputs)
  return inputs

@composite
def processed_module_input_set(draw):
  # TODO: processing turns a list of inputs into WHAT????
  # the easiest way I think to do this, would be to use an arbitrary module, and create inputs using it as a base
  # a thing which has the following properties
  # - all of the specific target inputs can be accessed via relative positioning
  # - all general inputs are stored together
  # - all aggregate inputs have been combined into one large input for each destination (specific or general) with aggregate inputs
  base_set = draw(module_input_set()) # pylint: disable=no-value-for-parameter
  proc_packs = {}
  agg_packs = {
    'ordered': {},
    'general': {}
  }
  ordered_packs = {}
  general_packs = {}
  # guaranteed order sort all non-aggregated type packs into the appropriate destination bucket
  # processing a module input set consists of a few parts
  #   - removing aggregate packages from the inputs
  #   - combining them in a guaranteed order
  #   - then readding a single entry per aggregated key
  # for pack in base_set.items():
  #   if pack[1].ctg_type is PackType.OVERLAY:
  #     proc_packs[pack[0]] = pack[1]
  #   elif pack[0] in agg_pack:
  #     agg_pack[pack[0]].append(pack[1])
  #   else:
  #     agg_pack[pack[0]] = pack[1]
  # proc_packs.update(agg_packs)
  # guaranteed order sort result aggregated packs into appropriate bucket
  # return results dict
  return base_set

@composite
def valid_module_input_set(draw):
  pass

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(PackType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self','']))
# def test_build_package_inputs(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_package_inputs(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_address = build_address(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = tuple([meld,sender_address])
#   self.assertEqual(inputs, res)

# @given(st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self', '']),
# st.sampled_from(RsrcType),
# st.sampled_from(PackType),
# st.sampled_from(FieldType),
# st.sampled_from(['SenderModuleId','self','Self']),
# st.sampled_from(['sender_set_id','self','Self','']))
# def test_build_package(self,rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id):
#   inputs = build_package(rm_id,rg_id,dp_resource,dp_type,dp_shape,sm_id,sg_id)
#   sender_address = build_address(sm_id,sg_id)
#   meld = build_meld(rm_id,rg_id,dp_resource,dp_type,dp_shape)
#   res = Package(meld,sender_address)
#   self.assertEqual(inputs, res)

# @composite
# def test_pack(draw,inputs):
#   """
#   but I need a guaranteed order to some of the inputs don't I?
#   Why? Bc agg type packages get combined in a spatially oriented way
#   Actually, bc of position data that is embedded in each sender we have a way to guarantee order of processing
#   Given that each sender has a position, this can be added to the package along with sender address (or in place of?)
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
#       st.sampled_from(PackType),
#       st.sampled_from(FieldType),
#       st.sampled_from(['SenderModuleId','self','Self']),
#       st.sampled_from(['sender_set_id','self','Self',''])))
#   pass
