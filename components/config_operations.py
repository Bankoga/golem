from components.config_reader import read

def build_full_config(config):
    for i,module in enumerate(config['Modules']):
        entry = build_module_entry(module)
        config['Modules'][i]=module['proc_groups'] = entry
    return module

def build_module_entry(module):
    proc = read(module['type_data']['proc'],'proc')
    result = module
    result['type_data'] = proc['type_data']
    for group in proc['group_details']:
        add group to proc_groups dict in results
    for stagegrouppair in stage_to_groups_dict:
        convert stage to group location,position data
    for input in inputs:
        add to the corresponding module level melds type dict
    for output in outputs:
        add to the corresponding module level melds type dict
    for hook_type in hooks:
        add this data somewhere
    for link in links_defined:
        add this data somewhere
    for link in links used:
        add this data somewhere
    return result