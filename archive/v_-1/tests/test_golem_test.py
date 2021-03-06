from yaml import load, dump
from golem import Golem


def String2SpikeEncoder(cur_str):
    return cur_str

def arith_brain():
    arithby = Golem('arith-brain')
    brain.build_self()
    ts = 0
    trns_sts = {}
    trn_strs = config = load(open('ab_trn_strs'))
    for trn_str in trn_strs:
        spike_data,actual = String2SpikeEncoder(trn_str)
        result = brain.activate(ts, spike_data)
        res_diff = diff(actual, result)
        brain.calc_reward(res_diff)
        ts++

    vld_sts = {}
    vld_strs = config = load(open('ab_vld_strs'))
    for vld_str in vld_strs:
        spike_data,actual = String2SpikeEncoder(trn_str)
        result = brain.activate(ts, spike_data)
        res_diff = diff(actual, result)
        TODO: L2FreezeNetworkPlasticity
        ts++

def build_full_config(brain_fname):
    # TODO: raise an exception and exit if the yaml does not exist
    config_fname = 'core\\configs\\brains\\{0}.yaml'.format(brain_fname)
    config = load(open(config_fname))

    for i, pd in enumerate(config['modules']):
        # TODO: raise an exception and exit if the yaml does not exist
        pd_conf_fname = 'core\\configs\\domain_types\\{0}.yaml'.format(pd['type'])
        pd_conf = load(open(pd_conf_fname))

        for j, region in enumerate(pd_conf['regions']):
            # TODO: raise an exception and exit if the yaml does not exist
            rconf_fname = 'core\\configs\\regions\\{0}.yaml'.format(region)
            rconf = load(open(rconf_fname))
            pd_conf['regions'][j] = rconf

        config['modules'][i]['type'] = pd_conf

    return config