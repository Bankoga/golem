from yaml import load, dump
from data.axioms.configs import dirs

"""
Plans:
This can be refactored into a slew of factories for reading,
    and validating different pieces using the same interface.
"""

def read(conf, ftype):
    reader = get_reader(ftype)
    return reader(conf,ftype)

def get_reader(ftype):
    if ftype == 'golem':
        return _read_from_golem
    elif ftype == 'proc':
        return _read_from_proc
    elif ftype == 'cdr':
        return _read_from_coder
    else:
        raise ValueError(ftype)

def _read_from_golem(conf,ftype):
    conf_fname = f'{dirs["golem"]}{conf}.{ftype}'
    try:
        with open(conf_fname) as f:
            return load(f)
    except FileNotFoundError as fnf_error:
        print(fnf_error)

def _read_from_proc(conf,ftype):
    conf_fname = f'{dirs["proc"]}{conf}.{ftype}'
    try:
        with open(conf_fname) as f:
            return load(f)
    except FileNotFoundError as fnf_error:
        print(fnf_error)

def _read_from_coder(conf,ftype):
    conf_fname = f'{dirs["cdr"]}{conf}.{ftype}'
    try:
        with open(conf_fname) as f:
            return load(f)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
