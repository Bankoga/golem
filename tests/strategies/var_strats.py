from hypothesis import strategies as st
from hypothesis.strategies import composite

from tests.strategies.pos_strats import valid_pos
from tests.strategies.prop_strats import arbitrary_id
from tests.strategies.packing_strats import full_address

@composite
def reg_item_var(draw):
  addr = draw(full_address()) # pylint: disable=no-value-for-parameter
  pos = draw(valid_pos()) # pylint: disable=no-value-for-parameter
  reg_id = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  reg_item = {
    'address': addr,
    'pos': pos,
    'reg_id': reg_id
  }
  return reg_item