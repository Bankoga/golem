import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.coders.coder_provider import coder_services
from data.axioms.configs import file_type, coder_ids
from tests.components.coders.test_coder import TestCoder
from utils.config_reader import read

class TestPartsSensor(TestCoder):

  def setUp(self):
    self.coder_id = coder_ids['ps']
    self.coder =  coder_services.get(self.coder_id, **{})
    self.coder_conf = read(self.coder_id,file_type['coder'])
  
if __name__ == '__main__':
  unittest.main()