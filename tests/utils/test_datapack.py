import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils.datapack import *
from string import ascii_lowercase
# from config_tests_data.py import *
from data.axioms.matrix import dest_key_pattern

class TestDataPack(unittest.TestCase):

  @given(st.tuples(st.from_regex(dest_key_pattern),st.text(),st.text()))
  def test_read_data(self,meld_tuple):
    datp=Datapack(meld_tuple)
    self.assertTrue(datp.address==meld_tuple[0])
    self.assertTrue(datp.resource==meld_tuple[1])
    self.assertTrue(datp.shape==meld_tuple[2])
    self.assertTrue(datp.type==f'{meld_tuple[0]}:{meld_tuple[1]}')


if __name__ == '__main__':
    unittest.main()