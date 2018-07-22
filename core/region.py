# contains the definition for the primary region object which will have two types
# this is the cortical stack, or thalamic relay stack level object
# perhaps the other sub cortical pieces could be a third type of region object. Wrapping all them together in an addressable manner

class Region():
     """
        determines region connection profile and layer organization
        possibilities are currently limited to
            - Cortex
            - Relay
        Currently, I plan to extend for a subcortical series of problem domains, though it may just be one domain with lots of regions
        perhaps the layers dict should be defined by the problem domain?
            But then where would the common region definitions exist?
            Where would the region to region connection profiles exist in that case?
    """
    layers_dict = {"Cortex":6, "Relay": 4}

    def __init__(self, region_key, length, width):
        self.name = region_key
        self.length = length
        self.width = width
         # could also be called height but num_layers is more useful
        self.num_layers = layers_dict[self.name]