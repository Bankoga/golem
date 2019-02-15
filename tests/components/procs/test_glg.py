from data.axioms.configs import proc_ids
from tests.components.procs.test_proc import TestProc

class TestGLG(TestProc):

  def __init__(self):
    super.__init__(proc_ids['glg'])