from components.func_groups.func_group import FuncGroup
from components.component import Component

class Module(Component):

  """
  Each module serves as a discrete env, and package repository for a set of func groups
  Responsible for aggregating packages with the same keys into single packages for routing
  """
  def __init__(self, proc):
    # once fully initialized, a module has very few aggregate properties to consider during operation
    self.proc = proc
    self.prev_activations=dict()
    self.groups=dict()
    self.input_shapes=dict()
    self._build_func_groups_()

  def _build_func_groups_(self):
    for group_id in self.proc.groups:
      group = self.proc.groups[group_id]
      self.groups[group_id] = FuncGroup(group, group.ctg_type)
      pass
    
  def process_inputs(self):
    pass

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