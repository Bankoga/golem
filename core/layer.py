# contains the definition for the layer object. Regions have multiple layers, and each layer contains an array of cells.
# layers are the primary cell container in this architecture

class Layer:
    
    TODO: Add a flag for point to cell or point to array of cells which change how the init works to avoid if clauses or other such checks during activation
    TODO: minimize the number of conditions to be checked during activation
    def __init__(self, config, source, location, length, width):
        """
        each region is composed of multiple layers and each layer spans the full length/width of the matrix
        region is 3D L x W x H, and each layer is a unit of height
        layer is 2D l x W, where each point is either a cell or an array of cells. The two types can't be mixed
        Either all points are cells, or all points are arrays
        regardless, a point in a layer of a region is a DESTINATION
        """
        TODO: implement region wide layers that do cell operations using addressess
        self.location = [location[len(location):] = [source]
        self.length = length
        self.width = width
        self.point_type = config['point_type'] #'cell' or 'array'
        self.morphs = config['cell_morphology']
        self.dests = config['destinations']
        self.destinations = create_destinations()
        # using the provided layer properties provided by the config, create the layer object
        """
        Local aspects of a layer and/or region that can differ
        - plasticity rules (inhib, excitory, modulatory) (timing, decay/potentiate funcs, etc...)
        - cell morphologys
        - allowed layer destinations (with blanks for cross-region, and cross-pd destination insertion. Example: cortical layer 5 and 6)
        - resource constraints (can each cell morphology have diff constraints?)
        - what else
        """

    def create_destinations(self):
        """
        given the region, and stack position, determine the connectivity profiles
            - region to region
            - layer to layer
            - problem domain to problem domain
                most layers inside the boundary of a problem domain will not connect to another problem domain
        determine the number of excitory and inhibitory cells for each morphology
        initialize all the cells
        """
        destinations = [][]
        return destinations

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
            the cortical region alone has 6 distinct layers with different output connection patterns, cell morphologys, plasticity rules, (what else?)
            There are at least 3 types of regions that I know need to be created, and at least two problem domains with undetermined regions
            Those other problem domains should at least have 1 type of region each, though they will likely have more than one
            So at this point, we can safely expect 5 or more regions that we need predefined to get info from
            Greater flexibility results from localizing cell morphologys, plas rules, resource constraints, connect patterns, etc... to each layer or region
        """