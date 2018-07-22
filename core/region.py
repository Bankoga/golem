# contains the definition for the primary region object which will have two types
# this is the cortical stack, or thalamic relay stack level object
# perhaps the other sub cortical pieces could be a third type of region object. Wrapping all them together in an addressable manner

class Region():
     """
        determines region connection profile and layer organization
        possibilities are currently limited to
            - Cortex
            - Relay
    """
    name = "Cortex"
    length = 0
    width = 0
    num_layers = 0 # could also be called height but num_layers is more useful
    layers_dict = {"Cortex":6, "Relay": 4}

    def __init__(self, region_type, length, width):
        name = region_type
        self.length = length
        self.width = width
        self.num_layers = layers_dict[name]