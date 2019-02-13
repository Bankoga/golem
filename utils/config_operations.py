from utils.config_reader import read

def build_full_config(config):
    for i,module in enumerate(config['modules']):
        entry = build_module_entry(module,i)
        config['modules'][i]=entry
    return module

def build_module_entry(module,m):
    proc = read(module['type_data']['proc'],'proc')
    result = module
    result['proc_type_data'] = proc['type_data']
    result['stages'] = []
    result['proc_groups'] = dict()
    for i,stage in enumerate(proc['stage_to_groups_dict']):
        # result['stages'][[stage['id']] = stage
        result['stages'].append(stage)
        for group in stage['groups']:
            result['proc_groups'][group]={
                    'id':group,
                    'pos_data':{'x':0,'y':m,'z':i}
                }
    for i,group in enumerate(proc['group_details']):
        result['proc_groups'][group['id']].update(group)
    for i,group in enumerate(proc['inputs']):
        if (proc['inputs'][group] is not None):
            result['inputs'].update(proc['inputs'][group])
    for i,group in enumerate(proc['outputs']):
        if (proc['outputs'][group] is not None):
            result['outputs'].update(proc['outputs'][group])
    result['hooks_into']=proc['hooks_into']
    result['hooks_outof']=proc['hooks_outof']
    result['links_defined']=proc['links_defined']
    result['links_used']=proc['links_used']
    return result