import unittest
from hypothesis import given
from hypothesis import strategies as st
from utils.pos import Pos

class TestPos(unittest.TestCase):
  
  @given(st.integers(),st.integers(),st.integers(),st.integers())
  def test_init_with_data(self,s,x,y,z):
    pos = Pos(s,x,y,z)
    self.assertEqual(pos.s,s)
    self.assertEqual(pos.x,x)
    self.assertEqual(pos.y,y)
    self.assertEqual(pos.z,z)
  
  def test_init_without_data(self):
    pos = Pos()
    self.assertEqual(pos.s,-1)
    self.assertEqual(pos.x,-1)
    self.assertEqual(pos.y,-1)
    self.assertEqual(pos.z,-1)