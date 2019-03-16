import numpy
import typing

from utils.pos import Pos

locale = ('address', 'pos')

class Address(typing.NamedTuple):
  golem: str
  matrix: str
  func_set: str
  stage: str
  group: str
  packager: str
  instruction: str
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
  source_id: str
  source_index: tuple
  filter_shape: tuple
  spacing_shape: tuple
  weights: list