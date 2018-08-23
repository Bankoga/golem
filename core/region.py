# contains the definition for the primary region object which will have two types
# this is the cortical stack, or thalamic relay stack level object
# perhaps the other sub cortical pieces could be a third type of region object. Wrapping all them together in an addressable manner
from yaml import load, dump
from layer import *
from location import *

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
    def __init__(self, key, ploc, region_type, length, width):
        """
        Initializes a new region object with the provided details, and config
        Size of the region is determined but the cells remain without axons, and dendrites
        """
        self.name = region_type
        TODO: Fix location data so that each level only needs to add its own key to the location.
        self.loc = Location(key, ploc)
        self.length = length
        self.width = width
        TODO: raise an exception and exit if the yaml does not exist
        config_fname = 'configs\\regions\\{0}.yaml'.format(region_type)
        self.config = load(open(config_fname))
        self.layers = self.create_layers()

    def create_layers(self):
        layers = dict()
        for l in self.config['layers']:
            # if the layers config object is an ordered list, then order is an unnecessary config item
            layers[l['name']] = Layer(l, self.loc, self.length, self.width)
        return layers
    
    TODO: expand activate to have current mode, time step, and the layer keyed input batched
    def activate(self):
        """
            perhaps a new name will better fit but this is fine for now. It matches the cell func name
            for each layer
                collect all the input axons based on the connectivity profiles from the axon server(?) into input batches for the layers
                collect the activation result of each layer on the input batch into an array
            return the layer results to the axon server for the current timestep
        """
        activations = []
        for l in layers:
            activations.extend(l.activate())
        return activations