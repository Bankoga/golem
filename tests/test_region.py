from yaml import load, dump
# import pytest
region_type = 'cortex'
config_fname = 'region_confs\\{0}.yaml'.format(region_type)
config = dump(load(open(config_fname)))

# from core.region import *
# r = Region("unknown", "cortex", 20, 20)

if the config layers object is a list, it preserves order of the layers
if it is a dict, it sorts them