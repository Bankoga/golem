# contains the definitions for the top level neural network object. brain_network
# herein lie the details for initialization, saving, and loading an entire network of distinct problem domains
# A brain_network consists of multiple problem domains wired together to form a cohesive dynamical system
# top level goals live here
from .imports import *
from yaml import load, dump
from layer import *

class BrainNetwork:
    def __init__(self, is_pair):
        TODO: determine where blank network standup, new network creation, and load network init should be handled
        self.pair = false # will be implemented using is_pair
        # at present the only other mode is maintenance which is toggled after running for the number of timesteps in the session_length
        self.mode = "work"
        self.ts_per_sim_second = 1000
        self.session_length = self.ts_per_sim_second * 60 * 12

    def create_network(self, brain_name):
        TODO: raise an exception and exit if the yaml does not exist
        config_fname = 'configs\\brains\\{0}.yaml'.format(brain_name)
        self.config = load(open(config_fname))
        self.name = self.config['name']
        TODO: parse each node, grab the config details, and build the nodes contents/destinations
        graph = {}
        i_counts = get_input_counts(self.config['nodes'])
        for pd in self.config['nodes']:
            TODO: add new problem domain to graph dict
            key = pd['name']
            num_cells = get_num_cells()
            obj = ProblemDomain(key, pd['type'], pd['outputs'], get_num_cells(i_counts[key]))
            graph.add(key, obj)
        self.brain = graph

    def get_input_counts(nodes):
        TODO: determine if this should instead return a dict of pd keys and input domains instead
        TODO: Determine method for calculating number of cells in a problem domain
        # Build adjacency matrix, and count number of inputs to each node?
        cells_dict = {}
        for pd in nodes:
            key = pd['name']
            count = 0
            inps = []
            for apd in nodes:
                if key != apd['name']:
                    if pd['outputs'].contains(key):
                        count += 1
                        inps.append(apd['name'])
            cells_dict.add(key, count, inps)
        return cells_dict

    def get_num_cells(self, edge_count):
        num_cells = 0
        TODO: use the edge count, and the size of the domain to determine the number of primary cells in the problem domain
        TODO: determine if this needs to be done at a lower level of abstraction. This seems likely
        return num_cells

    def batch_inputs(self, outputs):
        TODO: batch inputs to destinations based on their respective input profiles. Destinations or Cells can handle which cells deal with which sources
        TODO: Guarantee consistent order of sources in each bucket
        # this seems like a very problematic step
        """
        # buckets is a dictionary of dictionaries where list length is equal to the number of problem domains
        # each bucket (dictionary) is a collection of the outputs to destinations by level, or address
        buckets = {}
        sort all outputs based on dests
        for o in outputs:
            get bucket (pd name) key from o
            path_key is filled based on the switch
            At present partial paths are intended for neuromodulation not direct excitation or inhibition, thus are consumed by the destination
            switch dict based on length of path
                1 = all regions in pd partial
                    path_key = 'all_regions'
                2 = all layers in region partial
                    path_key = 'all_layers'
                3 = all dests in layer partial
                    path_key = 'all_dests'
                4 = specific destination. full path
                    path_key = layer_key
            if bucket key does not exist in buckets
                add bucket key dict to buckets
            if path_key array does not exist in bucket key dict
                add new path_key array to the bucket key dict with new item
            elif:
                append new item into path_key array in bucket key dict
        return buckets
        """

    def run(self):
        """
        create the repl to listen for external interrupts
        interrupt = self.loop()
        if interrupted by a REPL command
            - eval the interrupt
            - if pause, wait for new commands without looping
            - else if command shutsdown then terminate program
            - else if command is unrecognized throw an error message
            self.loop()
        """

    def loop(self):
        ts_count = 0
        #the ts_count can perhaps be used to create temporary objects that are released by the last cell to access it.
        # Each layer would this need to keep track of how many times it had been touched during the timestep, and self delete before returning
        """
        while waiting for interrupts run through a timestep
            - if ts_count >= session_length
                mode = "maintenance"
                - clear the old inputs
                inputs = []
                - activate each problem domain
                TODO: simply clearing the old inputs creates an inputs disconnect here that needs to be solved.
                    Implement clear so as to not affect sensory input collection
                - ts_count = 0
            - else:
                - collect sensory input
                    - should this be done inside the corresponding problem domain?
                    - where do external inputs plug into the network?
                    - how is that external data collected and translated into spikes?
                outputs.extend(sensor_data)
                # match axon destinations with problem domain accepted inputs
                inputs = self.batch_inputs(outputs)
                outputs = []
                for pd in self.brain:
                    # activate each problem domain (each PD activates it's region which in turn activate layers which activate cells)
                    # collect the ouputs from each problem domain
                    outputs.extend(pd.activate(mode, ts_count, inputs[pd.name]))
                TODO: where do the external outputs get sent at the end of a timestep?
                - ts_count++
        return interrupt
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