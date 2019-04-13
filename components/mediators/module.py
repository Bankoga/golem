from abc import abstractmethod
from components.base.plastic_comp import PlasticComp
from components.base.mechanisms.mediators.mediator import Mediator

from components.enums.pos import CtgType
from components.enums.prop_types import GroupType
from components.mediators.stage import Stage
from components.channels.misc_funcs import build_lineage

class Module(Mediator,PlasticComp):
  """
  A module is the top level processing region within a matrix
  It is a package production group
  each functional group in a matrix defines N things
    - an unique lineage
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
  Each module serves as a discrete env, and package repository for a set of func sets
  Responsible for aggregating packages with the same keys into single packages for routing

  Where do the inputs to these regions come from?
  The inputs are signal packages generated by other func sets
  """
  
  def __init__(self, *args, **kwargs):
    kwargs['ctg'] = CtgType.MODULE
    super().__init__(*args, **kwargs)
    # once fully initialized, a module has very few aggregate properties to consider during operation.
    # TODO: every group is at most, a 4x4 matrix of packagers!
    self.groups = dict()
    # self.prev_activations=dict()
    # self.input_shapes=dict()

  @property
  def module_type(self):
    return self.var[2]
  @module_type.setter
  def module_type(self, value):
    self.setter_error()

  def create_stages(self, stage_defs):
    stages = []
    for stage_def in stage_defs:
      # TODO: this is a stub that does not actually work
      stage = Stage(self.registry,stage_def['group_defs'])
      stages.extend(stage)
    return stages

  def build_details(self, *args, **kwargs):
    super().build_details(*args, **kwargs)

  # @abstractmethod
  # def process_inputs(self, inputs=None):
  #   raise NotImplementedError

  # def operate(self, inputs=None):
  #   super().operate()
    # proc_inputs = self.process_inputs(inputs)

  # @abstractmethod
  # def _build_func_(self):
  # def _build_funcs_(self):
  #   for set_id in self.groups:
  #     group = self.groups[set_id]
  #     self.groups[set_id] = (group, GroupType[group['group_type']])


  # @abstractmethod
  # def func(self, inputs):
  #   pass
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
  # def operate(self,inputShapes):
  #     outputShapes = prepareBlankOutputShapes()
  #     for group in self.processingGroups:
  #         # group.transform  needs to handle calculating its own activation shape which it adds to the outputShape to be processed by the primary dispatcher
  #         outputs = group.transform(inputShapes)
  #         for outputShape in outputs:
  #             outputShapes[outputShape.key]+=outputShape.value
  #             # If this is the last group, after adding the value, throw each point through a ReLU
  #     return outputShapes

    # self._set_hooks_()
    # self._set_links_defined_()
    # self._set_links_used_()

  # # @abstractmethod # pylint: disable=undefined-variable
  # def _set_hooks_(self):
  #   hook_prop = 'hooks'
  #   for hook_type in self.config[hook_prop]:
  #     for group in self.groups:
  #       if hook_prop not in self.groups[group]:
  #         self.groups[group][hook_prop] = [hook_type]
  #       else:
  #         self.groups[group][hook_prop].append(hook_type)

  # # @abstractmethod # pylint: disable=undefined-variable
  # def _build_links_(self, link_protos, link_results):
  #   if link_protos is not None:
  #     for link in link_protos:
  #       link_results[link['id']] = link
  #   return link_results

  # # @abstractmethod # pylint: disable=undefined-variable
  # def _set_links_defined_(self):
  #   links_defined = self.config['links_defined']
  #   link_defs = dict()
  #   self.link_definitions = self._build_links_(links_defined,link_defs)
  
  # # @abstractmethod # pylint: disable=undefined-variable
  # def _set_links_used_(self):
  #   links_used = self.config['links_used']
  #   prcd_lu = {}
  #   self.links_used = self._build_links_(links_used, prcd_lu)