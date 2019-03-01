from components.component import Component
from components.func_groups.fg_builder_provider import fg_services

from data.enums.pos import ComponentType

from utils.helpers.packer import build_address
class FuncGroup(Component):
  """
  A functional group is an addressable processing region within a matrix
  It is a package production group
  each functional group in a matrix defines N things
    - an unique address
    - the packages it produces
    - the rules for consuming the two types of packages: overlayed and aggregated
    - the types of packages it consumes that are module level
    - the links for extra output and/or output routing
  We currently have 
  - proc groups which breakdown into different proc types
    - cort cell distribution rule types
    - sub-cort cell distribution rule types
  - coder groups which breakdown into different coder types
    - sensors
    - motors

  Reward distribution rule types are not currently being worked upon
  That comes after we understand how the current pieces are turned into function groups
  """
  
  def __init__(self, group_id, group_type):
    super().__init__(group_id, group_type.get_component_type(), ctg_type=group_type)

  def get_id(self):
    return self.itm_id

  def get_type(self):
    return self.ctg_type

  def _build_func_(self):
    pass
  
  def func(self, inputs):
    pass
# def compose_functions(self,inputMelds,funcType,procStageGroupsDict,procStageShape,procGroupInputMelds,procGroupDetails,procGroupOutputMelds,procOutputMelds,shapeComposition,outputMelds,linkMelds,linksDefined):
# pass
# # just preparing a nice battery of for loops for all the looping that's gunna be done
# # for inMeld in inputMelds:
# # for outMeld in outputMelds:
# # for linkMeld in linkMelds:
# # for link in linksDefined:
# # for fType in funcType:
# # for stage in procStageGroupsDict:
# # for stageShape in procStageShape:
# # for groupInMeld in procGroupInputMelds:
# # for groupDetailSet in procGroupDetails:
# # for groupOutMeld in procGroupOutputMelds:
# # for procOutMeld in procOutputMelds:
# # for shapeComposition in shapeComposition:
# """
# at the lowest level of granularity, we have the actual functions
# It does not matter if these are cells, synapses, chemical interactions, processing groups, etc... because, whatever the lowest the level, that is where we combine all the pieces together.
# Currently, we are going with processing group level functions, however this could be turned into a object type property at some point.
# Preparation for processing, thus occurs in several steps
# 1) Build each function group from the proc groups
# 2) 
# ?) 
# //Converting all the input,output,and link melds into a dictionary that the processing groups can leverage for 
# """
# # return "lol"