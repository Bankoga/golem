from yaml import load, dump
from data.axioms.configs import dirs

class ConfigReader:
    def read(self, conf, ftype):
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
    golem_type_conf = load(open(conf_fname))
    return golem_type_conf

def _read_from_proc(conf):
    conf_fname = f'{dirs["proc"]}{conf}.proc'
    proc_type_conf = load(open(conf_fname))
    return proc_type_conf