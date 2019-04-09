from enum import Enum
# Hypothetically, each cell base could always implement its own function instead of specifiying convolutions

class CellType(Enum):
  UNSET = 1
  BASKET = 2
  BIPOLAR = 3
  CROWN = 4
  GRANULE = 5
  INV_CROWN = 6
  MAX_POOL_ALL = 7
  DENSE_POOL_SAME = 8
  PLATE = 9
  POINT = 10
  PYRAMID = 11
  ROSE = 12
  STAR = 13

cell_data = {
  'BASKET': {
    "collector_defs":[
      ["AB",[(4,4)]],
      ["S",[(4,4),(8,8),(12,12)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'BIPOLAR': {
    "collector_defs":[
      ["S",[(4,4),(8,8)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CROWN': {
    "collector_defs": [
      ["A",[(4,4)]],
      ["S",[(3,3)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'GRANULE': {
    "collector_defs":[
      ["A",[(1,1),(1,1),(1,1),(4,4),(8,8)]],
      ["B",[(8,8)]],
      ["S",[(3,3)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'INV_CROWN': {
    "collector_defs":[
      ["B",[(4,4)]],
      ["S",[(3,3)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'MAX_POOL_ALL': {
    "collector_defs":[
      ["ABS",[(5,5),(8,8)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'DENSE_POOL_SAME': {
    "collector_defs":[
      ["S",[(5,5)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'PLATE': {
    "collector_defs":[
      ["S",[(4,4),(8,8)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'POINT': {
    "collector_defs":[
      ["S",[(1,1)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'PYRAMID': {
    "collector_defs":[
      ["A",[(1,1),(1,1),(1,1),(4,4),(8,8)]],
      ["B",[(8,8)]],
      ["S",[(3,3)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'ROSE': {
    "collector_defs":[
      ["A",[(4,4)]],
      ["S",[(3,3)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'STAR': {
    "collector_defs":[
      ["ABS",[(4,4),(5,5),(6,6)]],
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'UNSET': {
    "collector_defs":[
      ["ABS",[(1,1)]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  }
}