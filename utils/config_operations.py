from components.config_reader import read

def build_full_config(config):
    for module in config['Modules']:
      read(module['Type'],'proc')