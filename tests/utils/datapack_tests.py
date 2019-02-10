import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils.datapack import *
from string import ascii_lowercase
# from config_tests_data.py import *

class DataPackTests(unittest.TestCase):
  @given(st.text(),st.text(),st.text())
  def test_read_data(self,address,resource,shape):
    datp=Datapack(address,resource,shape)
    self.assertIs(datp.address,address)
    self.assertIs(datp.resource,resource)
    self.assertIs(datp.shape,shape)