from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from components.axioms.matrix import max_resource_value, min_resource_value
from components.data.conv_shape import ConvShape
from tests.strategies.prop_strats import arbitrary_id
from tests.strategies.pos_strats import valid_pos, arb_addr

@composite
def valid_shape(draw):
  x = draw(st.just(ones((256,256))))
  st.assume(x.any())
  return x.shape
 
@composite
def valid_resource_data(draw):
  data = draw(st.builds(full,valid_shape(),st.decimals(min_value=min_resource_value,max_value=max_resource_value))) # pylint: disable=no-value-for-parameter
  st.assume(data.any())
  return data

@composite
def valid_conv_shape(draw):
  x = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  y = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  st.assume(x.any())
  z = ConvShape(x, y)
  return z

@composite
def valid_weights(draw):
  x = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  return ones(x)

@composite
def valid_locale(draw):
  res = {}
  return res

@composite
def valid_locale_inputs(draw):
  addr = draw(arb_addr()) # pylint: disable=no-value-for-parameter
  pos = draw(valid_pos()) # pylint: disable=no-value-for-parameter
  return (addr,pos)