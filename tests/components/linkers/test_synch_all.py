import utils.object_factory
from linkers.linker_provider import services
import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.configs import links

class TestSynchAll(unittest.TestCase):
  def test_SynchAllLinker(self):
    link_id = 'synch_all'
    linker = services.get(link_id, **{})
    self.assertTrue(linker.get_id(), link_id)
    self.assertTrue(False)
    
if __name__ == '__main__':
    unittest.main()