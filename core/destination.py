class Destination:

    def __init__(self, source, location, config):
        TODO: change how the destination init works based on cell size to avoid if clauses or other such checks during activation
        self.location = location.append(source)
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

    TODO: add timestep, and input batches to the activation method
    def activate(self):
        activations = []
        for c in cells:
            activations.extend(c.activate())
        return activations
