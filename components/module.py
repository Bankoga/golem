from components.func_groups.func_group import FuncGroup

class Module():

  """
  Each module serves as a discrete env, and datapack repository for a set of func groups
  Responsible for aggregating datapacks with the same keys into single datapacks for routing
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
      self.groups[group_id] = FuncGroup(group, group.type)
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