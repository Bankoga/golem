from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.data.collector_segment import CollectorSegment

from tests.strategies.data_strats import valid_shape
from tests.strategies.pos_strats import arb_addr, arb_label
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