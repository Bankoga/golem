from chainer import Variable

"""
A repository of helpers for the atypical convs used here
"""


def get_conv_sign(a, b):
  diff = 0
  if not (a.var is Variable and b.var is Variable):
    raise RuntimeError("One of the inputs is not a Variable!")
  elif a.shape < b.shape:
    diff = -1
  elif a.shape > b.shape:
    diff = 1
  return diff