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

    def __init__(self, region_type, length, width):
        self.name = region_type
        self.length = length
        self.width = width
        TODO: grab the yaml that corresponds to region_type, and raise an exception if it doesn't exist
        config_doc = region_type
        self.config = yaml.dump(yaml.load(config_doc))
        self.layers = create_layers()

    def create_layers(self):
        TODO: determine type of object for self.layers
         # could also be called height but num_layers is more useful
        # self.num_layers = layers_dict[self.name]
        layers = []
        """
        foreach distinct (layer_name, layer_details) in config.layers:
            create a new Layer() using the layer config, and the higher level destination data
            add the new layer to the layers object
            self.layer_config = self.get_layer_confs()
        """
        return layers
    
    def activate(self):
        """
            perhaps a new name will better fit but this is fine for now. It matches the cell func name
            for each layer
                collect all the input axons based on the connectivity profiles from the axon server(?) into input batches for the layers
                collect the activation result of each layer on the input batch into an array
            return the layer results to the axon server for the current timestep
        """