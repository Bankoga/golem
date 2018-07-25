# contains the definition for the problem domain level object
# e.g. a combination of a relay layer, and a cortex layer as initially devised
# will perhaps refactor in the future so as to include sub cortical aspects that are not the thalamus. It is still unclear how to do so though

class ProblemDomain():

    """
    as currently conceived, there are 4 types of problem domains
    - cortical | Relay -> Cortex | 2 Regions
    - subcortical | undetermined regions | ?
    - brainstem | undertermined regions | ?
    - cerebellum | cerebellum | 1
    Need to determine if give a number of cells to the domain, and have it determine the length and width of the regions
        If we assume yes, then what defines a problem domains inputs?
        Will position in the graph, and interdomain connectivity sufficiently differentiate PDs?
    Will currently operate under the hypothesis that Problem domains are largely defined by usage which is a function of types of inputs and outputs
    Consequently, can go with just num cells/columns/stacks for now
    """
    def __init__(self, name, domain_type, num_cells_primary):
        self.name = name
        self.regions # create the regions according to the domain_type definition
        # when creating cortical regions, num_cells_primary determines the num_columns, and num cells in the relays
        TODO: play around with efficiency of different lengths and widths instead of squares after all is working

    def activate(self):
        """
            perhaps a new name will better fit but this is fine for now. It matches the cell func name
            for each region
                collect all the input axons based on the connectivity profiles from the axon server(?) into input batches for the region
                collect the activation result of the region on the input batch into an array
            return the regions results to the axon server for the current timestep
        """