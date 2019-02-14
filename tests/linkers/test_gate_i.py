import utils.object_factory
from linkers.linker_provider import services
import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.configs import links

class TestGateI(unittest.TestCase):
  def test_GateLinker(self):
    link_id = 'gate_i'
    linker = services.get(link_id, **{})
    self.assertTrue(linker.get_id(), link_id)