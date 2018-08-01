# contains the workhose object definition. Herein lies the fundamental learning unit of the system, the cell
# While a cell will always live in some layer, some of it's init details come from each of it's higher level containers
# 
from axon import *
from chemical_state import *
from dendrite import *
from usage_limits import *

# should the cell accept a potential plasticity parameters object so that we can alter plasticity in other areas of the brain_network? Probably
class Cell():
    #methods
    def __init__(self, activation_type, cell_morphology, location, use_limits):
        """
         each cell should be able to handle its own initialization once given the necessary parameters from the higher levels
         probabilistically determine activation Type at the layer level (for inhib, and excitory. chem release cells will be dealt with later)
         set activaton type during init
         create dendrite connections to other layers in the same region according to the connectivity profile of the region type, as well as to other regions
         create axon connection to the other layers, regions, and problem domains
            according to the connectivity profile of the containing problem_domain in the network, the same region layer to layer profile,
            and the cross region layer to layer profile
        """
         #properties
         # 'inhibitory' || 'excitory' || 'modulatory' is determined by the containing layer and controls value of axon output
        self.activation_type = activation_type
        """"cell_morphology is determined by the containing layer
        controls the number of dendrites as well as their directions
        """
        TODO: determine the different types of cells that need to be accounted
        self.cell_morphology = cell_morphology
        self.cell_state = ChemicalState()
        # needs to be expanded to handle cells that are in sub-cortical regions and problem domains
        self.loc = location
        """
            input directions, and output destinations are determined by the location and cell_morphology
        """
        self.axon_output_directions = self.get_destinations()
        self.dendrite_input_directions = 
        self.output_terminals = Axon(activation_type, self.axon_output_directions)

        #activation props
        # use limits should be modifiable by the chemical state of the cell
        self.use_limits = use_limits
        TODO: determine acceptable depolarization rates
        self.depolarization_rate = 25
        self.ap_thresh = 100 # +- 75
        self.resting_potential = 0
        self.polarity = resting_potential

        #plasticity props
        self.threshhold_change_function
        self.stdp_window = 20 #timesteps
        TODO: what if instead of storing batch history, we count num steps since last use per synapse?
        uses num synapses * 2 instead of num synapses * 20
        though doing so does not track multiple uses within the stdp_window
        self.inputBatchHistory = "sigh" #fixed length array/matrix of length stdp_window or a stack of inputs

    def get_destinations():
        # all cells accept themselves as a destination that only they can read from
        # i.e. cells are addressable but are not the same as destinations
        """
        determines where the cell outputs to based on the location, cell_morphology, and inherited constraints
        connection variables
            - PD location in network
                - for adjacency (what is physically next to the current PD)
            - PD to PD
                - for the interPD output layers of the regions
                - for adjacency of dendrites across Regions
            - Region to Region
                - regions of the same type border each other based on PD adjacency
                - for the interRegion output layers of the various regions
            - Layer to Layer
                - which layers can output to which other layers in the same PD
                - which layers can output to layers of regions in adjacent PDs
                - which layers can output to other regions in the same PD
                - which layers can output to which layers of which regions of the output PDs
        PD location in graph
        """
        return []

    def maintenance():
        """
        reset axon fatigue
        reset cell chemical state
        reset dendrite sensitivity
        do scaling - should this happen before synapse creation?
            If it occurs before, then there might be more resources for new synapses.
            If it occurs after, then new synapses could immediately dissappear or be strengthened
        engage structural plasticity (i.e. synapseCreation)
        """

    def scaling():
        # ugh naming, and not sure where this needs to live nor how it's supposed to behave.....

    def threshhold_plasticity():

    def activate(self, mode, timestep, destination_state, input_batch):
        """
        TODO: determine if we need refactory/cooldown can't activate period
        if polarity >= ap_thresh: polarity -= (ap_thresh + depolarization_rate)
        else if polarity > restingPotential: polarity -= depolarization_rate
        if polarity < 0: polarity = 0
        send the input to the corresponding dendrites
        sum = summate each dendrite
        polarity += sum
        if polarity > apThreh:
            timeSinceLast = 0
            trigger stdp strengthen
            return axonStrength
        else:
            trigger stdp with timeSinceLast (if timeSinceLast > stdpWindow then there will be no change in synapses)
            return 0
        """

    def bar_update():
