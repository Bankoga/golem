# contains the definitions for cell dendrites
# includes initialization and destination based branching

# dendrites determine which destinations inputs are accepted from. Each axon goes to a specific destination
# any dendrite that accepts from that destination counts as being that destination

class Dendrite():
    #properties
    """ activation rates should be handled via usage limits
    dendrite_activation_rate # this might need to be handled on a per synapse per dendrite basis...... oh my
    curr_dendrite_sensitivity # again may be best to handled on a per synapse per dendrite basis..... sigh
    """
    synapse_weights # not the actual name because the form of the synapses has not yet been decided on. Placeholder reminder
    synapse_weight_limits = 0.2 to 100? # this needs work but so does everything.... waaa
    synapse_potentiation_weight_function
    synapse_decay_weight_function
    TODO: Determine if track the weight that was activated, time since active, or something other flag for use when calculating weight changes

    #methods
    def __init__(self, source_location):
        # each dendrite chain/tree/? should be able to handle its own initialization once given the necessary parameters from the higher levels
        # each dendrite knows the path key for the destination it pulls data from
        self.source = source_location
        TODO: what if instead of storing batch history, we count num steps since last use per synapse?
        # uses num synapses * 2 instead of num synapses * 20
        # though doing so does not track multiple uses within the stdp_window
        self.inputBatchHistory = "sigh" #fixed length array/matrix of length stdp_window or a stack of inputs

    def dendrite_sensitivity(self):
        dendrite_sensitivity_decay_function # perhaps this is just a method instead of a parameter

    def summate(self, input):
        total = 0
        """
        weights = multiply synapse array by the input array
        total = (sum of values in weights) * self.curr_sensitivity
        do plasticity
        """
        return total

    def synapse_plasticity(self, is_active):
        """
         implements the various synapse rules
         - use it or lose it
         - can only be 1
         - synapse resource competition / avg synapse weight / synapse weight distribution
         TODO: still undetermined if distance based decay of weighting will be implemented
        TODO: calculate sensitivity changes for the timestep based on is_active
        """

    def synapse_creation(self):
        """ for each synapse that is currently of 0 weight, and hasn't been just pruned, roll for creating a new synapse at a base creation weight """
        TODO: determine what works as a good weight starting weight for new synapses
        base_creation_weight = 10
        base_synapse_creation_probability = 0.3 +- 0.25
        for synapse in synapses:
            if synapse >= 0:
                roll for new synapse
                if roll > base_synapse_creation_probability:
                    add weight to synapse

    def synapse_prune():
        """ for all synapses below some threshhold weight are reduced to zero, and skipped during the next round of synapse creation """

    def reset():
        # oh my fuck what have I done?