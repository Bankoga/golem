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
        """
        Local aspects of a layer and/or region that can differ
        - plasticity rules (inhib, excitory, modulatory) (timing, decay/potentiate funcs, etc...)
        - cell types
        - allowed layer destinations (with blanks for cross-region, and cross-pd destination insertion. Example: cortical layer 5 and 6)
        - resource constraints (can each cell type have diff constraints?)
        - what else
        """

    
    def activate(self):
        """
            perhaps a new name will better fit but this is fine for now. It matches the cell func name
            collect all the input axons based on the connectivity profiles from the axon server(?) into input batches for the cells
            collect the activation result of each cell on the input batch into an array
            return the destinations set, and activation result array to the axon server for the current timestep
        """


    def get_destinations(self):
        """ since each region type has it's own layer types, where should destination mappings live?
        I feel that it may be best for layer destination mappings to live outside the class in a json, yaml, or other such file
        Why?
            the cortical region alone has 6 distinct layers with different output connection patterns, cell types, plasticity rules, (what else?)
            There are at least 3 types of regions that I know need to be created, and at least two problem domains with undetermined regions
            Those other problem domains should at least have 1 type of region each, though they will likely have more than one
            So at this point, we can safely expect 5 or more regions that we need predefined to get info from
            Greater flexibility results from localizing cell types, plas rules, resource constraints, connect patterns, etc... to each layer or region
        """