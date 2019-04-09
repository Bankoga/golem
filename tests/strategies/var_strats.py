from hypothesis import strategies as st
from hypothesis.strategies import composite

from tests.strategies.pos_strats import valid_pos, arb_lineage
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
def lineage_item_var(draw):
  lineage = draw(arb_lineage()) # pylint: disable=no-value-for-parameter
  reg_id = draw(arb_label()) # pylint: disable=no-value-for-parameter
  lineage_item = {
    'reg_id': reg_id,
    'lineage': lineage
  }
  return lineage_item

@composite
def lineage_item_valid_var(draw):
  # lineage_item = draw(st.fixed_dictionaries({'lineage': arb_lineage(),'pos': valid_pos(),'reg_id': arb_label()})) # pylint: disable=no-value-for-parameter
  lineage_item = draw(lineage_item_var()) # pylint: disable=no-value-for-parameter
  st.assume(lineage_item)
  return lineage_item

@composite
def channel_item_var(draw):
  recipient = draw(arb_lineage()) # pylint: disable=no-value-for-parameter
  sender = draw(arb_lineage()) # pylint: disable=no-value-for-parameter
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