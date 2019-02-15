import unittest
from hypothesis import given
import hypothesis.strategies as st
from data.axioms.configs import proc_ids
from components.procs.proc_provider import proc_services

class TestProcProvider(unittest.TestCase):

  @given(st.sampled_from(proc_ids.keys()))
  def test_get(self, proc_id):
    proc = proc_services.get(proc_ids[proc_id], **{})
    self.assertTrue(proc.get_id(), proc_ids[proc_id])

if __name__ == '__main__':
    unittest.main()