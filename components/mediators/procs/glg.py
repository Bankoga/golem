from components.mediators.procs.proc import Proc
from components.axioms.configs import proc_ids

class GLG(Proc):
  def __init__(self):
    super().__init__(proc_ids['glg'])

class GLGBuilder():
  def __init__(self):
    pass
  def __call__(self,**_ignored):
      return GLG()