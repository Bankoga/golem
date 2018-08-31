# contains the definitions for the top level neural network object. brain_network
# herein lie the details for initialization, saving, and loading an entire network of distinct problem domains
# A brain_network consists of multiple problem domains wired together to form a cohesive dynamical system
# top level goals live here
from .imports import *
from yaml import load, dump
from layer import *
from problem_domain import *
from decoder import *
from encoder import *

class ProblemGraph:
    def __init__(self, is_pair):
        self.pair = false # will be implemented using is_pair
        # at present the only other mode is maintenance which is toggled after running for the number of timesteps in the session_length
        self.mode = "work"
        self.ts_per_sim_second = 1000
        self.session_length = self.ts_per_sim_second * 60 * 12

    def build_graph(self, brain_fname, num_dests):
        self.desired_dests = num_dests
        self.build_full_config(brain_fname)
        self.name = self.config['name']
        graph = dict()
        TODO: parse each node, grab the config details, and build the nodes contents/destinations
        graph.extend(self.parse_decoders())
        graph.extend(self.parse_encoders())
        graph.extend(self.parse_problem_domains())
        TODO: determine size of each region, and layer so that cells can be stitched together
        i_counts = self.get_input_counts(graph)
        for node in graph:
            TODO: ensure that all nodes have a stitch method which fully populates cells with axons
            node.stitch(graph)
        TODO: Optim: pull all dests from all pds into a single adjacency list
        self.brain = graph

    def build_full_config(brain_fname):
        TODO: Larger architectures are going to have a huge config so maybe we should load and parse as needed...
        TODO: raise an exception and exit if the yaml does not exist
        config_fname = 'core\\configs\\brains\\{0}.yaml'.format(brain_fname)
        config = load(open(config_fname))
        for i, pd in enumerate(config['problem_domains']):
            TODO: raise an exception and exit if the yaml does not exist
            pd_conf_fname = 'core\\configs\\domain_types\\{0}.yaml'.format(pd['type'])
            pd_conf = load(open(pd_conf_fname))
            for j, region in enumerate(pd_conf['regions']):
                TODO: raise an exception and exit if the yaml does not exist
                rconf_fname = 'core\\configs\\regions\\{0}.yaml'.format(region)
                rconf = load(open(rconf_fname))
                pd_conf['regions'][j] = rconf
            config['problem_domains'][i]['type'] = pd_conf
        print(dump(config))
        self.config = config

    def parse_decoders(self):
        TODO: raise an exception if there are no decoders
        graph = dict()
        for pd in self.config['decoders']:
            key = pd['name']
            obj = Decoder(key, pd['type'], pd['output_dest'], pd['size'])
            graph[key] = obj
        return graph

    def parse_encoders(self):
        TODO: raise an exception if there are no encoders
        graph = dict()
        for pd in self.config['encoders']:
            key = pd['name']
            obj = Encoder(key, pd['type'], pd['input_source'], pd['outputs'], pd['size'])
            graph[key] = obj
        return graph

    def parse_problem_domains(self):
        TODO: raise an exception if there are no problem domains
        graph = dict()
        for pd in self.config['problem_domains']:
            key = pd['name']
            obj = ProblemDomain(key, pd['type'], pd['outputs'], i_counts[key])
            graph[key] = obj
        return graph

    def get_input_counts(self, nodes):
        TODO: Calculate minimum number of destinations supported by the provided architecture. This does require that the top level have a fully expanded copy of the brain config.
        TODO: Determine method for calculating number of dests consumed by each problem domain
        # use self.desired_dests and pd config info to determine how many dests are available to the problem domain during initialization
        TODO: use the edge count, and the size of the domain to determine the number of primary cells in the problem domain
        # though each level cumulatively effects the size of the problem graph, they have different impacts and consumption requirements
        TODO: determine how to handle non standard problem domains like the decoder, encoder, & subcortex
        # Build adjacency matrix, and count number of inputs to each node?
        self.desired_dests
        cells_dict = dict()
        for node in graph:
            key = node.name
            count = 0
            inps = []
            num_dests = 0
            for alt_node in graph:
                if key != alt_node.name:
                    if alt_node.outputs.contains(key):
                        count += 1
                        inps.append(alt_node.name)
            cells_dict[key] = count, inps, num_dests
        return cells_dict

    def batch_inputs(self, outputs):
        TODO: batch inputs based on their destination. The batched inputs will be passed by reference to cells for consumption.
        TODO: Guarantee consistent order of sources in each bucket
        TODO: Ensure that the aggregated sources are useable in a matrix mult
        # this seems like a very problematic step
        """
        # buckets is a dictionary of dictionaries where list length is equal to the number of problem domains
        # each bucket (dictionary) is a collection of the outputs to containers by level, or to specific destinations
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
        Blank network standup, new network creation, and load network should be handled by commands in the REPL
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