# contains the workhose object definition. Herein lies the fundamental learning unit of the system, the cell
# While a cell will always live in some layer, some of it's init details come from each of it's higher level containers
# 
from axon import *
from chemicalState import *
from dendrite import *


class UsageLimits():
    def __init__(self, capacity, cost, recharge):
        self.ts = 1000
        self.max_capacity = capacity # 300
        self.activation_cost = cost # 8
        self.capacity_recharge = recharge # 1
        self.adjusted_activation_cost = activation_cost - capacity_recharge
        self.time_till_depletion = max_capacity/adjusted_activation_cost
        self.raw_time_to_full = max_capacity/capacity_recharge
        self.recharge_one_activation = activation_cost / capacity_recharge
        self.max_init_freq = (time_till_depletion + ((ts-time_till_depletion) / (recharge_one_activation)))
        self.max_sustained_freq = max_capacity/recharge_one_activation * ts/max_capacity
        # self.console.log('num steps till depletion: ' + time_till_depletion + '\nsteps till full: ' + raw_time_to_full + '\nmax_init_freq: ' + max_init_freq + '\nmax_sustained_freq: ' + max_sustained_freq)
        """activity Counters
        simplistically, we could check frequency at intervals of N*time_period_of_interest but is doing so necessary?
        let's say that we are watching a section of a conveyor belt through a window
        upon said belt we can always see 10 buckets
        every time step, the bucket on the right disappears, while a new bucket on the left appears
        Each bucket has some probability of being filled with water, or having no water
        We want to count the number of buckets that currently have water as efficiently as possible in real time, as opposed to by time sampled frequency(?) (what?
        This is so that we can regulate the probability of seeing a full bucket in order to keep it within a range of values that we deem acceptable
        That being said, it seems like these rate limits could be a result of the dynamics of the system instead of explicitly enforced
        So it seems like counting the rate should be unnecessary
        If each full bucket has a resource cost, we have a max resource capacity, and we regain resources at fixed rate
            then the frequency should naturally have an upper limit based on some func of those parameters
        these params lead to max_init_freq of 162.5
            with max_freq of 125
    # baseline_activation_rate = 0
    # session_activation_rate = 0
    # st_activation_rate = 0
        activation_rate_boundaries # methinks that ARB will need to vary for cells in different locations, and for different types of cells.
        activation rate no longer seems necessary, and can be replaced with an activation_capacity, where each activation costs X resources, which it regains at a fixed rate.
        """

# should the cell accept a potential plasticity parameters object so that we can alter plasticity in other areas of the brainNetwork? Probably
class Cell():

    #methods
    def __init__(self, cell_type, location, use_limits):
        """
         each cell should be able to handle its own initialization once given the necessary parameters from the higher levels
         probabilistically determine cell Type at the layer level (for inhib, and excitory. chem release cells will be dealt with later)
         set cell type during init
         create dendrite connections to other layers in the same region according to the connectivity profile of the region type, as well as to other regions
         create axon connection to the other layers, regions, and problem domains
            according to the connectivity profile of the containing problemDomain in the network, the same region layer to layer profile,
            and the cross region layer to layer profile
        """
         #properties
        self.cell_type = cell_type
        self.cell_state = ChemicalState()
        # needs to be expanded to handle cells that are in sub-cortical regions and problem domains
        self.loc = location 
        """
            input directions, and output destinations are determined by the location and cell type
        """
        self.axon_output_directions
        self.dendrite_input_directions
        self.output_terminals = Axon(cell_type, location)

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
        self.inputBatchHistory = "sigh" #fixed length array/matrix of length stdp_window or a stack of inputs

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

    def activate(mode, layer_state, input_batch):
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
