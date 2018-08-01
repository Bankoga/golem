class Destination:

    def __init__(self, config, source, location, coord):
        TODO: change how the destination init works based on cell size to avoid if clauses or other such checks during activation
        self.location = location.extend([source, coord])
        self.point_size = config['point_size'] # num cells at the destination
        self.morphs = config['cell_morphology']
        self.dests = config['destinations']
        self.cells = create_cells()

    def create_cells(self):
        """
        create a number of cells equal to point_size, according to the rules for distribution, types, and destinations from the config
        """
        cells = []
        for i in range(0, self.point_size):
            cells.append(Cell())
        return cells

    TODO: add mode, time step, and input batches to the activation method
    def activate(self):
        activations = []
        for c in cells:
            activations.extend(c.activate())
        return activations

    def get_input_destinations(self):
        # return the list of locations that serve as sources for the cells at this destination
        # used for input batching
        """ since each region type has it's own layer types, where should destination mappings live?
        I feel that it may be best for layer destination mappings to live outside the class in a json, yaml, or other such file
        Why?
            the cortical region alone has 6 distinct layers with different output connection patterns, cell morphologys, plasticity rules, (what else?)
            There are at least 3 types of regions that I know need to be created, and at least two problem domains with undetermined regions
            Those other problem domains should at least have 1 type of region each, though they will likely have more than one
            So at this point, we can safely expect 5 or more regions that we need predefined to get info from
            Greater flexibility results from localizing cell morphologys, plas rules, resource constraints, connect patterns, etc... to each layer or region
        """