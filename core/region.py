# contains the definition for the primary region object which will have two types
# this is the cortical stack, or thalamic relay stack level object
# perhaps the other sub cortical pieces could be a third type of region object. Wrapping all them together in an addressable manner

class Region():
     """
        determines region connection profile and layer organization
        possibilities are currently limited to
            - Cortex
            - Relay
            - Cerebellum
        Currently, I plan to extend for a subcortical series of problem domains, though it may just be one domain with lots of regions
            As well as add a brain stem problem domain
            The issue with single PD subcort is that a single layer then actually be multiple layers which breaks the currentregion paradigm
            In a sense, a region adds "height" to a problem domain that is otherwise length and width onlys
        perhaps the layers dict should be defined by the problem domain? No. Problem Domain types define regions. Regions define layers
            But then where would the common region definitions exist? In a separate file or class
            Where would the region to region connection profiles exist in that case?
                If each region type is unique to a problem domain type, then R-R connections can be defined within the region type defs
    """
    # layers_dict = {"Cortex":6, "Relay": 4}

    def __init__(self, region_key, length, width):
        self.name = region_key
        self.length = length
        self.width = width
         # could also be called height but num_layers is more useful
        # self.num_layers = layers_dict[self.name]