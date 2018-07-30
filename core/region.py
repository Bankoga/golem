# contains the definition for the primary region object which will have two types
# this is the cortical stack, or thalamic relay stack level object
# perhaps the other sub cortical pieces could be a third type of region object. Wrapping all them together in an addressable manner
from yaml import load, dump
from layer import *

def str_to_class(str):
    return getattr(sys.modules[__name__], str)


class Region:
     """

            In a sense, a region adds "height" to a problem domain that is otherwise length and width onlys
        perhaps the layers dict should be defined by the problem domain? No. Problem Domain types define regions. Regions define layers
            But then where would the common region definitions exist? In a separate file or class
            Where would the region to region connection profiles exist in that case?
                If each region type is unique to a problem domain type, then R-R connections can be defined within the region type defs
    """

    def __init__(self, source, region_type, length, width):
        self.name = region_type
        self.location = [source]
        self.length = length
        self.width = width
        TODO: raise an exception if the yaml doesn't exist
        config_fname = 'region_confs\\{0}.yaml'.format(region_type)
        self.config = load(open(config_fname))
        self.layers = self.create_layers()

    def create_layers(self):
        TODO: determine type of object for self.layers
         # could also be called height but num_layers is more useful
        # self.num_layers = layers_dict[self.name]
        layers = []
        for i in self.config['layers']:
            # if I want to do something like name, morphs, dests, order = i.values() then I should be using an ordered dict
            name = i['name']
            # if the layers config object is an ordered list, then order is unnecessary
            # order = config.['order']
            [layers[len(layers):] = [Layer(config, self.name, self.location, self.length, self.width)]
        """
        foreach distinct (layer_name, layer_details) in self.config['layers']:
            create a new Layer() using the layer config, and self.location
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