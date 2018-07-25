# contains the definitions for the top level neural network object. brainNetwork
# herein lie the details for initialization, saving, and loading an entire network of distinct problem domains
# A brainNetwork consists of multiple problem domains wired together to form a cohesive dynamical system
# top level goals live here
from .imports import *

class BrainNetwork():
    mode = "work" # at present the only other mode is maintenance which is toggled after running for the number of timesteps in the session_length
    ts_per_sim_second = 1000
    session_length = ts_per_sim_second * 60 * 12

    def __init__(self):
        TODO: determine where blank network standup, new network creation, and load network init should be handled

    def run():
        tsCount = 0
        """
        create the repl to listen for external interrupts
        while waiting for interrupts run through a timestep
            - if tsCount >= session_length
                mode = "maintenance"
                - clear the old inputs
                - activate each problem domain
                TODO: simply clearing the old inputs creates an inputs disconnect here that needs to be solved.
                    Implement clear so as to not affect sensory input collection
                - tsCount = 0
            - else:
                - collect sensory input
                    - should this be done inside the corresponding problem domain?
                    - where do external inputs plug into the network?
                    - how is that external data collected and translated into spikes?
                - match axon destinations with problem domain accepted inputs
                - clear the old inputs
                - activate each problem domain
                - collect the ouputs from each problem domain
                TODO: where do the external outputs get sent at the end of a timestep?
                - tsCount++
        if interrupted by a REPL command
            - skip the loop
            - eval the command
            - if command pauses, wait for new commands without looping
            - else if command is unrecognized throw an error message
            - else if command shutsdown then terminate program
            - resume looping
        """

    def save(fn, a): 
        """Utility function that savess model, function, etc as pickle"""    
        pickle.dump(a, open(fn,'wb'))
    def load(fn): 
        """Utility function that loads model, function, etc as pickle"""
        return pickle.load(open(fn,'rb'))
    def load2(fn):
        """Utility funciton allowing model piclking across Python2 and Python3"""
        return pickle.load(open(fn,'rb'), encoding='iso-8859-1')

    def print_stats():
        """
        prints out connectivity stats about the network globally and per problem domain
        can be to screen or to csv
        columns: level, type, stats 
        examples:
            global, total, stats
            visual, total, stats
            visual, relay, stats
            visual, cortex, stats
        each problem domain has multiple sections
            - total
            - per each region
        the data that are printed
            - average ap thresh value
            - ap thresh value distributions
            - avg num synapses per cell
            - avg num possible synapses
            - avg num sets of synapses
            - num sets of synapses distributions
            - avg num synapses per set
            - avg synapse weight
            - synapse weight distributions
            - avg baseline activation rate
            - baseline activation rate distributions
        """

    def remap(self):
        # map a pre-existing network to a new network architecture.
        TODO: What degree of similarity between networks is required for this to work?