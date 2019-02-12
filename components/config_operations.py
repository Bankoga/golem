from components.config_reader import read

def build_full_config(config):
    for module in config['Modules']:
        entry = build_module_entry(module).popitem()
        module[entry.key] = entry.value
    return module

def build_module_entry(module):
    conf = read(module['Type'],'proc')
    conf
    return {"":""}