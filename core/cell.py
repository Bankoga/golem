# contains the workhose object definition. Herein lies the fundamental learning unit of the system, the cell
# While a cell will always live in some layer, some of it's init details come from each of it's higher level containers
# 
from axon import *
from chemical_state import *
from dendrite import *
from usage_limits import *
from location import *

# should the cell accept a potential plasticity parameters object so that we can alter plasticity in other areas of the brain_network? Probably
class Cell:
    TODO: Optim: move the cell constants to another file so that each cell does not duplicate unnecessary data
    def __init__(self, activation_type, cell_morphology, key, ploc, use_limits):
        """
        Creates a new cell given the necessary parameters from the higher levels
        probabilistically determine activation Type at the layer level (for inhib, and excitory. chem release cells will be dealt with later)
        sets the activaton type
        Cell init does not create axons, and dendrites
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
        self.loc = Location(key, ploc)
        """input directions, and output destinations are determined by the location and cell_morphology"""
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
        # need a min polarity in order to limit the depression of the cell
        self.polarity_min = -25
        # used as countdown untill it can process inputs again
        self.steps_since_active = 0
        # number of timesteps for the cooldown
        self.cooldown_duration = 3
        self.cooldown = self.cooldown_duration
        TODO: determine if the cooldown period should be longer than 1 timestep. 1 timestep can be handled by boolean

        #plasticity props
        self.threshhold_change_function
        self.stdp_window = 20 #timesteps

    def stitch(self, graph):
        """
        Create dendrite connections to other layers in the same region according to the connectivity profile of the region type, as well as to other regions
        Create axon connection to the other layers, regions, and problem domains
            according to the connectivity profile of the containing problem_domain in the network, the same region layer to layer profile,
            and the cross region layer to layer profile
        """

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
        if self.polarity >= self.ap_thresh:
            self.polarity -= (self.ap_thresh + self.depolarization_rate)
        elif self.polarity > self.resting_potential:
            self.polarity -= self.depolarization_rate
        elif self.polarity < self.polarity_min:
            self.polarity = self.polarity_min
        sum = 0
        send the input to the corresponding dendrites
        for dendrite in dendrites:
            sum += dendrite.summate(input_batch[dendrite.source])
        self.polarity += sum
        TODO: add refactory period to cell activation
        if self.cooldown >= self.cooldown_duration AND self.polarity > apThreh:
            self.time_since_last = 0
            self.cooldown = 0
            is_active = True
        else:
            self.time_since_last += 1
            self.cooldown += 1
            is_active = False
        trigger stdp with self.time_since_last (if self.time_since_last > self.stdp_window then there will be no change in synapses)
        return self.axon(is_active)

    def bar_update():

    def stitch(self, graph):
        """
        use the graph to build the axons, and dendrites
        """