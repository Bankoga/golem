lyrRls = {
  
}
lyrDtls = {}
inMlds = {}
outMlds = {}
gendShpDscrps = {}
lnks = {}

def parse_module_config():
    # each module should pass a consistency check between items listed in the melds and items used in the function dict
    # As well as check items listed in the function dict and used in the output melds and link melds
  return "lol"


def parse_gt_config(golem_type, num_dests, is_pair):
    """
    validate inputs
    check for a valid golem type file in the golem type database (lol. it's a directory for the MVP)
    throw an error for existance of validation operational violations
    ctags --options=C:\Users\sturmy\.vscode\extensions\ms-python.python-2018.12.1\resources\ctagOptions --languages=Python --exclude=**/site-packages/** -o d:\Projects\golem-factory\.vscode\tags .
Install Universal Ctags Win32 to enable support for Workspace Symbols
Download the CTags binary from the Universal CTags site.
Option 1: Extract ctags.exe from the downloaded zip to any folder within your PATH so that Visual Studio Code can run it.
Option 2: Extract to any folder and add the path to this folder to the command setting.
Option 3: Extract to any folder and define that path in the python.workspaceSymbols.ctagsPath setting of your user settings file (settings.json).
    """
    config_fname = 'core\\configs\\golem_types\\{0}.yaml'.format(golem_type)
    golem_type_config = load(open(config_fname))
    # core_config = self.build_full_config(golem_type_config['core_type_fname'])
    settings = golem_type_config.extend({
        'desired_base_dests': num_dests,
        'paired': is_pair, #should be capable of handling through config as well at some point
        # 'core_config': core_config
        #'core_type_fname': config.core_type_fname. CORE_TYPE or CORE_TYPE_FNAME SHOULD BE INCLUDED IN GOLEM_TYPE config already
    })
    return settings

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

def build_full_config(core_type_fname):
    TODO: Larger architectures are going to have a huge config so maybe we should load and parse as needed...
    TODO: raise an exception and exit if the yaml does not exist
    config_fname = 'core\\configs\\golem_core_types\\{0}.yaml'.format(core_type_fname)
    config = load(open(config_fname))
    print(dump(config))
    return config

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

def evaluate_melds():
    """
    when evaluating a config there are several list categories of properties that need to be generated
        - categories: fields, modules, links, inputMelds, outputMelds, linkMelds
        - properties: referenced categories, unreferenced categories
        - 
    we start with a list of modules which, if well formed, will have all the data necessary and referenced. Otherwise we throw error
    for each module
        globally collect inputMelds,outputMelds,linkMelds
        locally collect procGroupInputMelds,procGroupDetails,procGroupOutputMelds
        convert and procStageGroupsDict into the "function_data" module config property
        convert and add ShapeDictList into the dict of all shapes
    for each item in inputMelds,outputMelds,linkMelds:
        replace template components
    for each link in inputMelds,outputMelds,linkMelds:
        expand links descriptions into full links
    try {
        validate_all()
    }
    throw (validation_error err){
        do error things
        hard fail out
        return
    }
    return updated_configs
    """