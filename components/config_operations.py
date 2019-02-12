from components.config_reader import read

def build_full_config(config):
    for module in config['Modules']:
        build_full_module_entry(module)

def build_module_entry(module):
    read(module['Type'],'proc')
