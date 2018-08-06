from yaml import load, dump
# import pytest

cort = dump(load(open('region_confs\\cortex.yaml')))
relay = dump(load(open('region_confs\\relay.yaml')))

# from core.region import *
# r = Region("unknown", "cortex", 20, 20)

if the config layers object is a list, it preserves order of the layers
if it is a dict, it sorts them

def calc_mem_use(num_cells, edges_per_cell, cell_size):
    py_edge_size = 96
    byts = (num_cells * cell_size) + (num_cells * edges_per_cell * py_edge_size)
    print('{0} terabytes'.format(byts / Math.pow(10,12)))
    return 'wtf have I done?'