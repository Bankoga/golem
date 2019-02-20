import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils.datapack import Datapack

from data.axioms.configs import dest_key_pattern

class TestDataPack(unittest.TestCase):

  def setUp(self):
    # In order to test all the variants for the integration, we will need BDD tests
    self.datp = Datapack(tuple('Self-Destination_id-Subdestination_id'), 'GLG')
  
  @given(st.tuples(st.from_regex(dest_key_pattern),st.text(),st.text()))
  def test_read_data(self,meld_tuple):
    datp=Datapack(meld_tuple)
    self.assertTrue(datp.address==meld_tuple[0])
    self.assertTrue(datp.resource==meld_tuple[1])
    self.assertTrue(datp.shape==meld_tuple[2])
    self.assertTrue(datp.type==f'{meld_tuple[0]}:{meld_tuple[1]}')

  def test_format_address_on_valid_data(self):
    self.assertTrue(self.datp.address, 'GLG-Destination_id-Subdestination_id')

  def test_format_address_on_well_formed_invalid_data(self):
    pass

  def test_format_address_on_random_data(self):
    pass

if __name__ == '__main__':
    unittest.main()