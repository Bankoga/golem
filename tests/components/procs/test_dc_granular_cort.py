import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.procs.proc_provider import proc_services
from data.axioms.configs import file_type, proc_ids
from tests.components.procs.test_proc import TestProc
from utils.config_reader import read


class TestDCGranularCort(TestProc):

  def setUp(self):
    self.proc_id = proc_ids['dcgc']
    self.proc =  proc_services.get(self.proc_id, **{})
    self.proc_conf = read(self.proc_id,file_type['proc'])
  
if __name__ == '__main__':
  unittest.main()