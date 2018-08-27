from yaml import load, dump

def build_full_config(brain_fname):
    # TODO: raise an exception and exit if the yaml does not exist
    config_fname = 'core\\configs\\brains\\{0}.yaml'.format(brain_fname)
    config = load(open(config_fname))

    for i, pd in enumerate(config['problem_domains']):
        # TODO: raise an exception and exit if the yaml does not exist
        pd_conf_fname = 'core\\configs\\domain_types\\{0}.yaml'.format(pd['type'])
        pd_conf = load(open(pd_conf_fname))

        for j, region in enumerate(pd_conf['regions']):
            # TODO: raise an exception and exit if the yaml does not exist
            rconf_fname = 'core\\configs\\regions\\{0}.yaml'.format(region)
            rconf = load(open(rconf_fname))
            pd_conf['regions'][j] = rconf

        config['problem_domains'][i]['type'] = pd_conf

    return config