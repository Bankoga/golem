from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.matrix.address_registry import AddressRegistry

from tests.strategies.prop_strats import arb_label

@composite
def addr_reg(draw):
  lbl = draw(arb_label()) # pylint: disable=no-value-for-parameter
  reg = AddressRegistry(label=lbl)
  return reg