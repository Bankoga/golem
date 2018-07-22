# contains the definitions for cell dendrites
# includes initialization and destination based branching

# dendrites determine which destinations inputs are accepted from. Each axon goes to a specific destination
# any dendrite that accepts from that destination counts as being that destination

class Dendrite():
    #properties
    dendrite_activation_rate # this might need to be handled on a per synapse per dendrite basis...... oh my
    curr_dendrite_sensitivity # again may be best to handled on a per synapse per dendrite basis..... sigh
    synapse_weights # not the actual name because the form of the synapses has not yet been decided on. Placeholder reminder
    synapse_weight_limits = 0.2 to 100? # this needs work but so does everything.... waaa
    synapse_potentiation_weight_function
    synapse_decay_weight_function

    #methods
    def __init__(self):
        # each dendrite chain/tree/? should be able to handle its own initialization once given the necessary parameters from the higher levels

    def dendrite_sensitivity():
        dendrite_sensitivity_decay_function # perhaps this is just a method instead of a parameter

    def dendrite_summation():

    def synapse_plasticity():
        """
         implements the various synapse rules
         - use it or lose it
         - can only be 1
         - synapse resource competition / avg synapse weight / synapse weight distribution
         TODO: still undetermined if distance based decay of weighting will be implemented
        """

    def synapse_creation():
        """ for each synapse that is currently of 0 weight, and hasn't been just pruned, roll for creating a new synapse at a base creation weight """
        TODO: determine what works as a good weight starting weight for new synapses
        baseCreationWeight = 10
        base_synapse_creation_probability = 0.3 +- 0.25

    def synapse_prune():
        """ for all synapses below some threshhold weight are reduced to zero, and skipped during the next round of synapse creation """

    def reset():
        # oh my fuck what have I done?