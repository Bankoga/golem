from yaml import load, dump
# import pytest

cort = dump(load(open('region_confs\\cortex.yaml')))
relay = dump(load(open('region_confs\\relay.yaml')))

# from core.region import *
# r = Region("unknown", "cortex", 20, 20)

if the config layers object is a list, it preserves order of the layers
if it is a dict, it sorts them