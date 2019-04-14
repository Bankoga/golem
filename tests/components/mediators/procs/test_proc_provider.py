import unittest

import hypothesis.strategies as st
from hypothesis import given

from components.mediators.procs.proc_provider import proc_services
from components.axioms.configs import proc_ids


class TestProcProvider(unittest.TestCase):

  @given(st.sampled_from(sorted(proc_ids.keys())))
  def test_get(self, proc_id):
    proc = proc_services.get(proc_ids[proc_id], **{})
    self.assertTrue(proc.get_id(), proc_ids[proc_id])

if __name__ == '__main__':
    unittest.main()
