import numpy
import typing

locale = ('address', 'pos')

class ConvVar(typing.NamedTuple):
  source_id: str
  source_index: tuple
  filter_shape: tuple
  spacing_shape: tuple
  weights: list