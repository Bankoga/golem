from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from components.axioms.data import var_types
from components.axioms.matrix import max_resource_value, min_resource_value
from components.data.conv_shape import ConvShape
from tests.strategies.prop_strats import arbitrary_id
from tests.strategies.pos_strats import valid_pos

@composite
def valid_shape(draw):
  x = draw(valid_conv_shape()) # pylint: disable=no-value-for-parameter
  return x.f_shape

@composite
def valid_resource_data(draw):
  data = draw(st.builds(full,valid_shape(),st.decimals(min_value=min_resource_value,max_value=max_resource_value))) # pylint: disable=no-value-for-parameter
  st.assume(data.any())
  return data

@composite
def valid_conv_shape(draw):
  x = draw(st.just(ones((256,256))))
  st.assume(x.any())
  arb_id = draw(arbitrary_id()) # pylint: disable=no-value-for-parameter
  p = draw(valid_pos()) # pylint: disable=no-value-for-parameter
  y = ConvShape(arb_id, p, x.shape, (1,1))
  st.assume(y)
  return y