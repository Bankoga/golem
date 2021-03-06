import numpy
import typing

from utils.pos import Pos
from utils.helpers.properter import build_lineage_id

locale = ('lineage', 'pos')
# var_types = ['pos', 'f_shape', 's_shape', 'weights']

class Lineage(typing.NamedTuple):
  """
  Lineagees are container positions at levels within a matrix.
  """
  golem: str = None
  matrix: str = None
  module: str = None
  stage: str = None
  group: str = None
  packager: str = None
  instruction: str = None
  channel: str = None

  def __str__(self):
    return build_lineage_id(self)

# items must be filled in the correct order without skipping!

# class Graph(typing.NamedTuple):
#   space: type of space
#   points: set of points in the space
#   edges: list of edges between points

# class DataLocale(typing.NamedTuple):
#   pass

# class WorkerLocale(typing.NamedTuple):
#   lineage: Lineage

# class MediatorLocale(WorkerLocale):
#   incoming: list
#   outgoing: list