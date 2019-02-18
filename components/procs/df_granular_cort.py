from components.procs.proc import Proc
from data.axioms.configs import proc_ids

class DFGranularCort(Proc):
  def __init__(self):
    super().__init__(proc_ids['dfgc'])

class DFGranularCortBuilder():
  def __init__(self):
    pass
  def __call__(self,**_ignored):
      return DFGranularCort()