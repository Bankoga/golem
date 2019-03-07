import unittest

from hypothesis import given
from hypothesis import strategies as st

from utils.conv_shape import ConvShape

class TestConvShape(unittest.TestCase):
  def setUp(self):
    self.f_shape = (4,4)
    self.s_shape = (1,1)
    self.cs = ConvShape(self.f_shape,self.s_shape)

  def test_init(self):
    self.assertEqual(self.cs.f_shape,self.f_shape)
    self.assertEqual(self.cs.s_shape,self.s_shape)

if __name__ == '__main__':
  unittest.main()