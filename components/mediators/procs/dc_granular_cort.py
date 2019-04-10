from components.mediators.procs.proc import Proc
from components.axioms.configs import proc_ids

class DCGranularCort(Proc):
  def __init__(self):
    super().__init__(proc_ids['dcgc'])

class DCGranularCortBuilder():
  def __init__(self):
    pass
  def __call__(self,**_ignored):
      return DCGranularCort()