from utils.object_factory import *
from data.axioms.configs import proc_ids
from components.procs.glg import GLGBuilder
# from components.procs.dm import DmLinkerBuilder
# from components.procs.gate_i import GateILinkerBuilder
# from components.procs.synch_i import SynchILinkerBuilder
# from components.procs.synch_all import SynchAllLinkerBuilder

class ProcProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, proc_id, **kwargs):
    return self.create(proc_id, **kwargs)

proc_services = ProcProvider()
proc_services.register_builder(proc_ids['glg'], GLGBuilder())
# proc_services.register_builder(proc_ids['?'], ?Builder())
# proc_services.register_builder(proc_ids['?'], ?Builder())
# proc_services.register_builder(proc_ids['?'], ?Builder())
# proc_services.register_builder(proc_ids['?'], ?Builder())