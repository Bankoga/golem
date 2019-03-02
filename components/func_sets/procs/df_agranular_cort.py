from components.func_sets.procs.proc import Proc
from data.axioms.configs import proc_ids

class DFAgranularCort(Proc):
  def __init__(self):
    super().__init__(proc_ids['dfagc'])

class DFAgranularCortBuilder():
  def __init__(self):
    pass
  def __call__(self,**_ignored):
      return DFAgranularCort()