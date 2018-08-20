# contains the definition for the layer object. Regions have multiple layers, and each layer contains an array of cells.
# layers are the primary cell container in this architecture
import numpy as np
from destination import *

class Layer:
    TODO: minimize the number of conditions to be checked during activation
    def __init__(self, config, source, location, length, width, index):
        """
        Creates a new layer according the provided config, and details.
        Size is determined by the containing region.
        Cells must be wired together separately.
        """
        """
        each region is composed of multiple layers and each layer spans the full length/width of the matrix
        region is 3D L x W x H, and each layer is a unit of height
        layer is 2D l x W, where each point is either a cell or an array of cells. The two types can't be mixed
        Either all points are cells, or all points are arrays
        regardless, a point in a layer of a region is a DESTINATION
        """
        TODO: implement region wide layers that do cell operations using addressess
        TODO: determine name vs index for the path data
        self.name = config['name']
        self.index = index
        self.location = location.append(source)
        self.length = length
        self.width = width
        self.config = config
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
        destinations = np.zeros(shape=(self.length,self.width))
        for i in range(0, self.length):
            for j in range (0 self.width):
                destinations[i][j] = Destination(self.config, self.index, self.location, [i,j])
        return destinations

    TODO: expand activate to have the current mode, time step, and the destination keyed input batches
    def activate(self):
        """
            perhaps a new name will better fit but this is fine for now. It matches the cell func name
            collect all the input axons based on the connectivity profiles from the axon server(?) into input batches for the cells
            collect the activation result of each cell on the input batch into an array
            return the destinations set, and activation result array to the axon server for the current timestep
        """
        activations = []
        for i in range(0, self.length):
            for j in range (0 self.width):
                activations.extend(self.destinations[i][j].activate())
        return activations