from hypothesis import strategies as st
from hypothesis.strategies import composite

from components.matrix.lineage_registry import LineageRegistry

from tests.strategies.prop_strats import arb_label

@composite
def lineage_reg(draw):
  lbl = draw(arb_label()) # pylint: disable=no-value-for-parameter
  reg = LineageRegistry(label=lbl)
  return reg