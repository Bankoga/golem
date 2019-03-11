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
  'CellType.BASKET': {
    "cnv_tmplts":[
      ["AB",["4x4"]],
      ["AB",["8x8,1"]],
      ["S",["4x4","8x8,1","12x12,2"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.BIPOLAR': {
    "cnv_tmplts":[
      ["S",["4x4"],["8x8,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.CROWN': {
    "cnv_tmplts": [
      ["A",["4x4"]],
      ["A",["8x8,1"]],
      ["S",["3x3"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.GRANULE': {
    "cnv_tmplts":[
      ["A",["1x1","1x1","1x1","4x4","8x8"]],
      ["B",["8x8,1"]],
      ["S",["3x3"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.INV_CROWN': {
    "cnv_tmplts":[
      ["B",["4x4"]],
      ["B",["8x8,1"]],
      ["S",["3x3"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.MAX_POOL_ALL': {
    "cnv_tmplts":[
      ["*",["NxN"],["8x8,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.DENSE_POOL_SAME': {
    "cnv_tmplts":[
      ["S",["NxN"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.PLATE': {
    "cnv_tmplts":[
      ["S",["4x4","8x8,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.POINT': {
    "cnv_tmplts":[
      ["S",["1x1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.PYRAMID': {
    "cnv_tmplts":[
      ["A",["1x1","1x1","1x1","4x4","8x8"]],
      ["B",["4x4"]],
      ["B",["8x8,1"]],
      ["S",["3x3"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.ROSE': {
    "cnv_tmplts":[
      ["A",["4x4"]],
      ["A",["8x8,1"]],
      ["S",["3x3"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  'CellType.STAR': {
    "cnv_tmplts":[
      ["*",["4x4","5x5","6x6"]],
      ["*",["8x8,1","10x10,1","12x12,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  }
}