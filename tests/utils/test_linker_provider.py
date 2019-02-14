import utils.object_factory
from utils.linker_provider import linkers
import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.configs import links

class TestLinkerProvider(unittest.TestCase):
  @given(st.sampled_from(links))
  def test_get(self, link_id):
    linker = linkers.get(link_id, **{})
    self.assertTrue(linker.get_id(), link_id)

  def test_LoopILinker(self):
    link_id = 'loop_i'
    self.test_get(link_id)
    self.assertTrue(False)
  
  def test_DmLinker(self):
    link_id = 'dm'
    self.test_get(link_id)
    self.assertTrue(False)

  def test_GateLinker(self):
    link_id = 'gate_i'
    self.test_get(link_id)
    self.assertTrue(False)

  def test_SynchILinker(self):
    link_id = 'synch_i'
    self.test_get(link_id)
    self.assertTrue(False)

  def test_SynchAllLinker(self):
    link_id = 'synch_all'
    self.test_get(link_id)
    self.assertTrue(False)
