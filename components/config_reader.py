from yaml import load, dump
from data.axioms.configs import dirs

def read(conf, ftype):
    reader = get_reader(ftype)
    return reader(conf)

def get_reader(ftype):
    if ftype == 'golem':
        return _read_from_golem
    elif ftype == 'proc':
        return _read_from_proc
    else:
        raise ValueError(ftype)

def _read_from_golem(conf):
    conf_fname = f'{dirs["golem"]}{conf}.golem'
    with open(conf_fname) as f:
        return load(f)

def _read_from_proc(conf):
    conf_fname = f'{dirs["proc"]}{conf}.proc'
    with open(conf_fname) as f:
        return load(f)
