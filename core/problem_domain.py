# contains the definition for the problem domain level object
# e.g. a combination of a relay layer, and a cortex layer as initially devised
# will perhaps refactor in the future so as to include sub cortical aspects that are not the thalamus. It is still unclear how to do so though
from yaml import load, dump
from layer import *
from location import *

class ProblemDomain:
    """
    Need to determine if give a number of cells to the domain, and have it determine the length and width of the regions
        If we assume yes, then what defines a problem domains inputs?
        Will position in the graph, and interdomain connectivity sufficiently differentiate PDs?
    Will currently operate under the hypothesis that Problem domains are largely defined by usage which is a function of types of inputs and outputs
    Consequently, can go with just num cells/columns/stacks for now
    """
    def __init__(self, name, domain_type, outputs, num_cells_primary):
        """
        Initialization creates a new problem domain using the provided details, and selected config
        Size is determined during initialization, but cells remain without axons, and dendrites
        """
        self.name = name
        self.loc = Location(name)
        TODO: raise an exception and exit if the yaml does not exist
        config_fname = 'configs\\domain_types\\{0}.yaml'.format(domain_type)
        self.config = load(open(config_fname))
         # create the regions according to the domain_type definition
        self.regions = self.create_regions()
        # when creating cortical regions, num_cells_primary determines the num_columns, and num cells in the relays
        TODO: play around with efficiency of different lengths and widths instead of squares after all is working

    def create_regions(self):
        regions = dict()
        for r in self.config['regions']:
            regions[r] = Region(r, self.loc)
        return regions

    TODO: add activation parameters to activate
    def activate(self):
        """
            perhaps a new name will better fit but this is fine for now. It matches the cell func name
            for each region
                collect all the input axons based on the connectivity profiles from the axon server(?) into input batches for the region
                collect the activation result of the region on the input batch into an array
            return the regions results to the axon server for the current timestep
        """
        activations = []
        for r in self.regions:
            activations.extend(r.activate())
        return activations

    def stitch(self, graph):
        """
        Takes an initialized graph without axons, and dendrites.
        Adds axons, and dendrites to the problem domain based on the details stored in the graph.
        """
        TODO: account for pass by reference, and either ensure no side effects xor entirely use side effects
        # new_graph = graph
        # old_graph = graph