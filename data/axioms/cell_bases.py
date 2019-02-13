# Hypothetically, each cell base could always implement its own function instead of specifiying convolutions
node_types = {
  "Basket": {
    "type":"cell",
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
  "Bipolar": {
    "type":"cell",
    "cnv_tmplts":[
      ["S",["4x4"],["8x8,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  "Crown": {
    "type":"cell",
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
  "Granule": {
    "type":"cell",
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
  "InvCrown": {
    "type":"cell",
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
  "MaxPoolAll": {
    "type":"cell",
    "cnv_tmplts":[
      ["*",["NxN"],["8x8,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  "DensePoolSame": {
    "type":"cell",
    "cnv_tmplts":[
      ["S",["NxN"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  "Plate": {
    "type":"cell",
    "cnv_tmplts":[
      ["S",["4x4","8x8,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  "Point": {
    "type":"cell",
    "cnv_tmplts":[
      ["S",["1x1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  "Pyramid": {
    "type":"cell",
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
  "Rose": {
    "type":"cell",
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
  "Star": {
    "type":"cell",
    "cnv_tmplts":[
      ["*",["4x4","5x5","6x6"]],
      ["*",["8x8,1","10x10,1","12x12,1"]]
    ],
    "freq_range": [5,256],
    "init_freq": 5,
    "pct_of_pod": 0,
    "init_threshhold":0.98,
    "activation_function":"tanh"
  },
  "function": {
    "type":"function"
  }
}