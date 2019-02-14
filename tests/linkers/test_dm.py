import utils.object_factory
from linkers.linker_provider import services
import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.configs import links

class TestDM(unittest.TestCase):
  def test_DmLinker(self):
    link_id = 'dm'
    linker = services.get(link_id, **{})
    self.assertTrue(linker.get_id(), link_id)