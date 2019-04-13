from components.base.mechanisms.mechanism import Mechanism
from components.enums.pos import CtgType
from components.cogs.cells.cell import Cell

class Group(Mechanism):
  def __init__(self, *args, **kwargs):
    kwargs['ctg'] = CtgType.GROUP
    super().__init__(*args,**kwargs)

  @property
  def group_type(self):
    return self.var[1]
  @group_type.setter
  def group_type(self,value):
    self.setter_error()

  @property
  def source_index(self):
    return self.var[2]
  @source_index.setter
  def source_index(self,value):
    self.setter_error()
    
  @property
  def source_shape(self):
    return self.var[3]
  @source_shape.setter
  def source_shape(self,value):
    self.setter_error()

  @property
  def pct_of_stage(self):
    return self.var[4]
  @pct_of_stage.setter
  def pct_of_stage(self,value):
    self.setter_error()

  @property
  def nodes_details(self):
    return self.var[5]
  @nodes_details.setter
  def nodes_details(self,value):
    self.setter_error()
  
  def create_nodes(self, node_labels,nodes_details):
    nodes = []
    for i,node_details in enumerate(nodes_details):
      node = {
        'node': Cell(self.registry,
                    node_details['node_type'],
                    node_details['resources_accepted'],
                    self.source_index,
                    self.source_shape,
                    label=node_labels[i]),
        'pct_of_group': node_details['pct_of_group']
      }
      nodes.append(node)
    return nodes
  
  def __eq__(self,other):
    return (self.label == other.label
            and self.group_type == other.group_type
            and self.source_index == other.source_index
            and self.source_shape == other.source_shape
            and self.nodes_details == other.nodes_details)