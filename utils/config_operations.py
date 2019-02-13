from utils.config_reader import read

def build_full_config(config):
    for i,module in enumerate(config['modules']):
        build_module_entry(module,i)
        config['modules'][i]=module
    return config

def build_module_entry(module,m):
    proc = read(module['type_data']['proc'],'proc')
    module['proc_type_data'] = proc['type_data']
    module['stages'] = []
    module['proc_groups'] = dict()
    for i,stage in enumerate(proc['stage_to_groups_dict']):
        # module['stages'][[stage['id']] = stage
        module['stages'].append(stage)
        for group in stage['groups']:
            module['proc_groups'][group]={
                    'id':group,
                    'pos_data':{'x':0,'y':m,'z':i}
                }
    if proc['group_details'] is not None:
        for i,group in enumerate(proc['group_details']):
            module['proc_groups'][group['id']].update(group)
    if proc['inputs'] is not None:
        for i,group in enumerate(proc['inputs']):
            if (proc['inputs'][group] is not None):
                module['inputs'].extend(proc['inputs'][group])
    if proc['outputs'] is not None:
        for i,group in enumerate(proc['outputs']):
            if (proc['outputs'][group] is not None):
                module['outputs'].extend(proc['outputs'][group])
    module['hooks_into']=proc['hooks_into']
    module['hooks_outof']=proc['hooks_outof']
    module['links_defined']=proc['links_defined']
    module['links_used']=proc['links_used']