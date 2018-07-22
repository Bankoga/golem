# contains the definition for the layer object. Regions have multiple layers, and each layer contains an array of cells.
# layers are the primary cell container in this architecture

class Layer():
    
    def __init__(self):
        """
        given the region, and stack position, determine the connectivity profiles
            - region to region
            - layer to layer
            - problem domain to problem domain
                most layers inside the boundary of a problem domain will not connect to another problem domain
        determine the number of excitory and inhibitory cells
        initialize all the cells
        """
    
    def activate():
        """
            perhaps a new name will better fit but this is fine for now. It matches the cell func name
            collect all the input axons based on the connectivity profiles from the axon server(?) into input batches for the cells
            collect the activation result of each cell on the input batch into an array
            return the destinations set, and activation result array to the axon server for the current timestep
        """


