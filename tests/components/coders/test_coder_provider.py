import unittest
from hypothesis import given
import hypothesis.strategies as st
from data.axioms.configs import coder_ids
from components.coders.coder_provider import coder_services

class TestCoderProvider(unittest.TestCase):

  @given(st.sampled_from(sorted(coder_ids.keys())))
  def test_get(self, coder_id):
    coder = coder_services.get(coder_ids[coder_id], **{})
    self.assertTrue(coder.get_id(), coder_ids[coder_id])

if __name__ == '__main__':
    unittest.main()