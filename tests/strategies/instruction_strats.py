from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.data.collector_segment import CollectorSegment

from tests.strategies.data_strats import valid_shape
from tests.strategies.prop_strats import arb_resource_type
from tests.strategies.pos_strats import arb_addr, arb_label,arb_step_directions
from components.vars.data import Address

@composite
def valid_collector_segment(draw):
  x = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  addr = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  label = draw(arb_label()) # pylint: disable=no-value-for-parameter
  si = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  st.assume(x and si and addr and label)
  st.assume(type(addr) == Address)
  z = CollectorSegment(address=addr,source_index=si,fill_shape=x,label=label)
  return z

@composite
def arb_full_collector_def(draw):
  step_directions = draw(arb_step_directions()) # pylint: disable=no-value-for-parameter
  steps_shapes = draw(st.lists(elements=st.tuples(st.integers(),st.integers())))
  resource_type = draw(arb_resource_type()) # pylint: disable=no-value-for-parameter
  st.assume(step_directions and steps_shapes and resource_type)
  return [step_directions, steps_shapes, resource_type]