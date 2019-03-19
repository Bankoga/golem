from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.matrix.address_registry import AddressRegistry

from tests.strategies.prop_strats import arbitrary_id

@composite
def addr_reg(draw):
  lbl = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  reg = AddressRegistry(label=lbl)
  return reg