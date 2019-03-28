from hypothesis import strategies as st
from hypothesis.strategies import composite


from components.data.collector_segment import CollectorSegment

from tests.strategies.data_strats import valid_shape

@composite
def valid_collector_segment(draw):
  x = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  y = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  st.assume(x.any())
  z = CollectorSegment(x, y)
  return z