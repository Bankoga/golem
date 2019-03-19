import numpy
import typing

from utils.pos import Pos

locale = ('address', 'pos')
# var_types = ['pos', 'f_shape', 's_shape', 'weights']

class Address(typing.NamedTuple):
  golem: str = None
  matrix: str = None
  func_set: str = None
  stage: str = None
  group: str = None
  packager: str = None
  instruction: str = None
  channel: str = None


# items must be filled in the correct order without skipping!

# class Graph(typing.NamedTuple):
#   space: type of space
#   points: set of points in the space
#   edges: list of edges between points

# class DataLocale(typing.NamedTuple):
#   pass

# class WorkerLocale(typing.NamedTuple):
#   addr: Address

# class MediatorLocale(WorkerLocale):
#   incoming: list
#   outgoing: list

class ConvVar(typing.NamedTuple):
  filter_shape: tuple
  spacing_shape: tuple
  weights: list