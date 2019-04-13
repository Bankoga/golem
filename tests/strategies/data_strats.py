from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from components.axioms.matrix import max_resource_value, min_resource_value
from tests.strategies.prop_strats import arb_label,arb_resource_type
from tests.strategies.pos_strats import valid_pos, arb_lineage
from utils.helpers.chaos import draw as draw_num

@composite
def valid_shape(draw):
  x = draw(st.just(ones((256,256))))
  st.assume(x.any())
  return x.shape

@composite
def arb_percentage(draw):
  pct = draw(st.floats(min_value=0.00000002, max_value=1))
  st.assume(pct)
  return pct

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
  data = draw(st.builds(full,valid_shape(),st.floats(min_value=min_resource_value,max_value=max_resource_value))) # pylint: disable=no-value-for-parameter
  st.assume(data.any())
  return data

@composite
def valid_resource_data_and_index(draw):
  data = draw(valid_resource_data()) # pylint: disable=no-value-for-parameter
  st.assume(data.any())
  i = draw_num(data.shape[0])
  j = 0
  if len(data.shape) > 1:
    j = draw_num(data.shape[1])
  return (data, i, j)

@composite
def valid_resource_array(draw, shape=valid_shape(), num_shapes=st.integers(max_value=30)): # pylint: disable=no-value-for-parameter
  r_set = []
  ns = draw(num_shapes)
  for i in range(ns): # pylint: disable=unused-variable
    r_set.append(draw(valid_resource_data())) # pylint: disable=no-value-for-parameter
  return r_set

@composite
def arb_resource_set(draw):
  st.lists(elements=arb_resource_type(), unique=True) # pylint: disable=no-value-for-parameter


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
  lineage = draw(arb_lineage()) # pylint: disable=no-value-for-parameter
  pos = draw(valid_pos()) # pylint: disable=no-value-for-parameter
  return (lineage,pos)