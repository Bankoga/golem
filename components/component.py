from data.enums.pos import ComponentType

class Component:
  # TODO: implement a base class that is shared across all components
  def __init__(self, component_id,component_type, ctg_type=None):
    """
    component_id : the semantic key used as reference for the component object
    component_type : the semantic key used as reference for the component functionality within the matrix
    """
    self.ctg_type = ctg_type
    self.itm_id = component_id
    self.op_lvl = ComponentType(component_type)

  def get_id(self):
    return self.itm_id