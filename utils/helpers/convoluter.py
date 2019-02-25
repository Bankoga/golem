from chainer import Variable

"""
A repository of helpers for the atypical convs used here
"""


def get_conv_sign(inp_shape, out_shape):
  conv_sign = 0
  if inp_shape > out_shape:
    conv_sign = -1
  elif inp_shape < out_shape:
    conv_sign = 1
  return conv_sign