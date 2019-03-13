from hypothesis import strategies as st
from hypothesis.strategies import composite

from tests.strategies.pos_strats import valid_pos, arb_addr
from tests.strategies.prop_strats import arbitrary_id

@composite
def reg_item_var(draw):
  reg_id = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  reg_item = {
    'reg_id': reg_id
  }
  return reg_item

@composite
def reg_item_valid_var(draw):
  reg_item = draw(reg_item_var()) # pylint: disable=no-value-for-parameter
  st.assume(reg_item)
  return reg_item

@composite
def addr_item_var(draw):
  addr = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  pos = draw(valid_pos()) # pylint: disable=no-value-for-parameter
  reg_id = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  addr_item = {
    'address': addr,
    'pos': pos,
    'reg_id': reg_id
  }
  return addr_item

@composite
def addr_item_valid_var(draw):
  # addr_item = draw(st.fixed_dictionaries({'address': arb_addr(),'pos': valid_pos(),'reg_id': arbitrary_id()})) # pylint: disable=no-value-for-parameter
  addr_item = draw(addr_item_var()) # pylint: disable=no-value-for-parameter
  st.assume(addr_item)
  return addr_item