from hypothesis import strategies as st
from hypothesis.strategies import composite

from tests.strategies.pos_strats import valid_pos, arb_addr
from tests.strategies.prop_strats import arb_label

@composite
def reg_item_var(draw):
  reg_id = draw(arb_label()) # pylint: disable=no-value-for-parameter
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
  reg_id = draw(arb_label()) # pylint: disable=no-value-for-parameter
  addr_item = {
    'reg_id': reg_id,
    'address': addr
  }
  return addr_item

@composite
def addr_item_valid_var(draw):
  # addr_item = draw(st.fixed_dictionaries({'address': arb_addr(),'pos': valid_pos(),'reg_id': arb_label()})) # pylint: disable=no-value-for-parameter
  addr_item = draw(addr_item_var()) # pylint: disable=no-value-for-parameter
  st.assume(addr_item)
  return addr_item

@composite
def channel_item_var(draw):
  recipient = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  sender = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  reg_id = draw(arb_label()) # pylint: disable=no-value-for-parameter
  channel_item = {
    'reg_id': reg_id,
    'recipient': recipient,
    'sender': sender
  }
  return channel_item

@composite
def channel_item_valid_var(draw):
  channel_item = draw(channel_item_var()) # pylint: disable=no-value-for-parameter
  st.assume(channel_item)
  return channel_item