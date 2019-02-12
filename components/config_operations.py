from components.config_reader import read

def build_full_config(config):
    for i,module in enumerate(config['Modules']):
        entry = build_module_entry(module)
        config['Modules'][i]=module['proc_groups'] = entry
    return module

def build_module_entry(module):
    conf = read(module['type_data']['proc'],'proc')
    build_module_groups(module)
    return conf

def build_module_groups(module):
    return {"":""}