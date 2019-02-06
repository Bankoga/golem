lyrRls = {
  
}
lyrDtls = {}
inMlds = {}
outMlds = {}
gendShpDscrps = {}
lnks = {}

def parse_module_config():
  return "lol"

def module_function_builder(lyrRls, lyrDtls, inMlds, outMlds, gendShpDscrps, lnks):
  return "lol"

def init_ts(ts_data):
    TODO: Pull ts level global data into config for use in other files for num ts calcs. MWAHAHAHAAAA
    # plan is to have simulated sec defined, and num ts per sec evald to see how fast it compares to analagous physically implemented systems. Does it have more time than us?
    self.ts_per_sim_second = ts_data['ts_per_sec']#1000
    self.session_length = self.ts_per_sim_second * ts_data['session_length'] #60 * 60 * 12
    TODO: determine timestep vs update cycle ontology

def generate_golem_id(golem_type):
    rh = 0#calc random 1024-hex hash
    cts = 0#get current timestamp()
    return '{0}-{1}-{2}'.format(golem_type, rh, cts)

def assemble_egg(self, config, core_type_fname, num_dests):
    egg = {
        'config': config,
        'name': config['name'],
        'ts': init_ts(config['ts_data'])
    }
    graph = dict()
    TODO: parse each node, grab the config details, and build the nodes contents/destinations
    graph.extend(self.parse_decoders(egg))
    graph.extend(self.parse_encoders(egg))
    graph.extend(self.parse_modules(egg))
    TODO: determine size of each region, and layer so that cells can be stitched together
    i_counts = self.get_input_counts(graph, num_dests)
    for node in graph:
        TODO: ensure that all nodes have a stitch method which fully populates cells with axons
        node.stitch(graph)
    TODO: Optim: pull all dests from all pds into a single adjacency list
    TODO: Build relay problem domain out of region
    return egg.extend({'graph': graph, 'id': self.generate_golem_id(self.golem_type)})

def build_full_config(core_type_fname):
    TODO: Larger architectures are going to have a huge config so maybe we should load and parse as needed...
    TODO: raise an exception and exit if the yaml does not exist
    config_fname = 'core\\configs\\golem_core_types\\{0}.yaml'.format(core_type_fname)
    config = load(open(config_fname))
    TODO: rename problem domains to modules?
    for i, pd in enumerate(config['modules']):
        TODO: raise an exception and exit if the yaml does not exist
        pd_conf_fname = 'core\\configs\\domain_types\\{0}.yaml'.format(pd['type'])
        pd_conf = load(open(pd_conf_fname))
        for j, region in enumerate(pd_conf['regions']):
            TODO: raise an exception and exit if the yaml does not exist
            rconf_fname = 'core\\configs\\regions\\{0}.yaml'.format(region)
            rconf = load(open(rconf_fname))
            pd_conf['regions'][j] = rconf
        config['modules'][i]['type'] = pd_conf
    print(dump(config))
    return config

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

def parse_modules(self):
    TODO: raise an exception if there are no problem domains
    graph = dict()
    for pd in self.config['modules']:
        key = pd['name']
        obj = ProblemDomain(key, pd['type'], pd['outputs'], i_counts[key])
        graph[key] = obj
    return graph

def get_input_counts(self, nodes, desired_dests):
    TODO: Calculate minimum number of destinations supported by the provided architecture. This does require that the top level have a fully expanded copy of the brain config.
    TODO: Determine method for calculating number of dests consumed by each problem domain
    # use desired_dests and pd config info to determine how many dests are available to the problem domain during initialization
    TODO: use the edge count, and the size of the domain to determine the number of primary cells in the problem domain
    # though each level cumulatively effects the size of the golem, they have different impacts and consumption requirements
    TODO: determine how to handle non standard problem domains like the decoder, encoder, & subcortex
    # Build adjacency matrix, and count number of inputs to each node?
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