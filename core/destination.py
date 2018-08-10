class Destination:

    def __init__(self, config, source, location, coord):
        TODO: change how the destination init works based on cell size to avoid if clauses or other such checks during activation
        TODO: Confirm that inits do not mutate variables passed to them by accident
        self.location = location.extend([source, coord])
        self.point_size = config['point_size'] # num cells at the destination
        self.morphs = config['cell_morphology']
        self.dests = config['destinations']
        self.cells = self.create_cells()

    def create_cells(self):
        """
        create a number of cells equal to point_size, according to the rules for distribution, types, and destinations from the config
        # each cell type takes up a % of the num cells (point_type)
        cell_type_distribution contains tuples of current count, max count given point_size,
            and cell type data as calcd via the provided % of num cell type, and cell type data
        """
        TODO: should distribution data be determined via a prop in the init so that we can look at it later?
        cell_type_distribution = self.get_distributions()
        cells = []
        for i in range(0, self.point_size):
            c, cell_type_distribution = self.get_cell(cell_type_distribution)
            cells.append(c)
        return cells

    def get_distributions(self):
        """
        ct_dist = []
        max_count = 0
        ind = 0
        ind_of_max = 0
        total_count = 0
        for each cell type
            calc floored ct_max_num via cell type prob * point_size
            total_count += ct_max_num
            append new tuple for current count, max count
            if max_count < ct_max_num:
                ind_of_max = ind
            ind++
        count_diff = total_count - self.point_size
        increase ct_max_num of ct_dist[ind_of_max] by count_diff
        return ct_dist
        """

    def get_cell_data(self, ct_dist):
        """
        grab copy of first cell type tuple
        if current count >= num cell - 1:
            remove first tuple from list
        elif:
            increment current count in the ct_dist
        use cell type dist to create
        c = Cell(DETAILS)
        return new cell, and ct_dist
        """

    TODO: add mode, time step, and input batches to the activation method
    def activate(self):
        activations = []
        TODO: eval the chem state then consume all partials to ascertain effects on the chemical state
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
        TODO: determine if this is handled by the dendrites class