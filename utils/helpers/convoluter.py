from chainer import Variable

"""
A repository of helpers for the atypical convs used here
"""


def get_conv_sign(inp_pack, out_pack):
  conv_sign = 0
  if inp_pack.var > out_pack.var:
    conv_sign = -1
  elif inp_pack.var < out_pack.var:
    conv_sign = 1
  return conv_sign