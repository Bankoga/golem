from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from components.axioms.matrix import max_resource_value, min_resource_value
from components.data.collector_segment import CollectorSegment
from tests.strategies.prop_strats import arb_label
from tests.strategies.pos_strats import valid_pos, arb_addr
from utils.helpers.prop_gen_help import draw as draw_num

@composite
def valid_shape(draw):
  x = draw(st.just(ones((256,256))))
  st.assume(x.any())
  return x.shape

@composite
def valid_sz_shape_and_index(draw):
  x = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  i = draw_num(x[0])
  sz = draw_num(x[0]/2)
  res = (x,(i),sz)
  if len(x) >1:
    j = draw_num(x[1])
    sz = draw_num(min(x[0]/2,x[1]/2))
    res = (x,(i,j),sz)
  return res

@composite
def valid_shape_and_index(draw):
  x = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  i = draw_num(x[0])
  res = (x,(i))
  if len(x) >1:
    j = draw_num(x[1])
    res = (x,(i,j))
  return res
 
@composite
def valid_resource_data(draw):
  data = draw(st.builds(full,valid_shape(),st.decimals(min_value=min_resource_value,max_value=max_resource_value))) # pylint: disable=no-value-for-parameter
  st.assume(data.any())
  return data

@composite
def valid_resource_array(draw, shape=valid_shape(), num_shapes=st.integers(max_value=30)): # pylint: disable=no-value-for-parameter
  r_set = []
  ns = draw(num_shapes)
  for i in range(ns):
    r_set.append(draw(valid_resource_data())) # pylint: disable=no-value-for-parameter
  return r_set

@composite
def valid_collector_segment(draw):
  x = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  y = draw(valid_shape()) # pylint: disable=no-value-for-parameter
  st.assume(x.any())
  z = CollectorSegment(x, y)
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