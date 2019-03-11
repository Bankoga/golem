from hypothesis import strategies as st
from hypothesis.strategies import composite
from numpy import full, ones

from components.axioms.data import var_types

@composite
def var_pair(draw,elements=st.one_of(st.sampled_from(sorted(var_types)))):
  var_type = draw(elements)
  st.assume(var_type)
  return var_type