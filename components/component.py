class Component:
  # TODO: implement a base class that is shared across all components
  def __init__(self, component_id,component_type):
    """
    component_id : the semantic key used as reference for the component object
    component_type : the semantic key used as reference for the component functionality within the matrix
    """
    self.id = component_id
    self.type = component_type