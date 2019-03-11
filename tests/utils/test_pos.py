import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.pos import Floor, Dimension

from utils.pos import Pos
from tests.strategies.pos_strats import valid_pos, ctg_prop,dimension_prop

class TestPos(unittest.TestCase):
  
  @given(st.text())
  def test_invalid_init(self,comp_type):
    with self.assertRaises(ValueError):
      Pos(comp_type)
      
  @given(ctg_prop(),st.integers(),st.integers(),st.integers(),st.integers(),st.integers(),st.integers()) # pylint: disable=no-value-for-parameter
  def test_init_with_data(self,comp_type,floor,x,y,z,r,c):
    pos = Pos(comp_type,floor,x,y,z,r,c)
    self.assertEqual(pos.comp_type, comp_type)
    self.assertEqual(pos.floor,floor)
    self.assertEqual(pos.x,x)
    self.assertEqual(pos.y,y)
    self.assertEqual(pos.z,z)
    self.assertEqual(pos.r,r)
    self.assertEqual(pos.c,c)
  
  @given(ctg_prop()) # pylint: disable=no-value-for-parameter
  def test_init_without_data(self, comp_type):
    pos = Pos(comp_type)
    self.assertEqual(pos.floor,Floor.WAREHOUSE)
    self.assertEqual(pos.x,-1)
    self.assertEqual(pos.y,-1)
    self.assertEqual(pos.z,-1)
    self.assertEqual(pos.r,-1)
    self.assertEqual(pos.c,-1)

  @given(valid_pos()) # pylint: disable=no-value-for-parameter
  def test_hash(self, pos):
    self.assertEqual(pos.get_hash(), hash((pos.comp_type,pos.floor,pos.x,pos.y,pos.z,pos.r,pos.c)))

  @given(valid_pos(), dimension_prop()) # pylint: disable=no-value-for-parameter
  def test_get_dim_value(self,pos,dim):
    if dim in Dimension:
      result = pos.get_dim_value(dim)
      if dim is Dimension.OP_LVL:
        expectation = pos.comp_type.value
      elif dim is Dimension.FLOOR:
        expectation = pos.floor.value
      elif dim is Dimension.LENGTH:
        expectation = pos.x
      elif dim is Dimension.WIDTH:
        expectation = pos.y
      elif dim is Dimension.HEIGHT:
        expectation = pos.z
      elif dim is Dimension.ROW:
        expectation = pos.r
      elif dim is Dimension.COLUMN:
        expectation = pos.c
        self.assertEqual(result,expectation)
    else:
      with self.assertRaises(ValueError):
        pos.get_dim_value(dim)