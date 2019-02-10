import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils.datapack import *
from string import ascii_lowercase
# from config_tests_data.py import *

class DataPackTests(unittest.TestCase):

  @given(st.tuples(st.text(),st.text(),st.text()))
  def test_read_data(self,meld_tuple):
    datp=Datapack(meld_tuple)
    self.assertIs(datp.address,meld_tuple[0])
    self.assertIs(datp.resource,meld_tuple[1])
    self.assertIs(datp.shape,meld_tuple[2])