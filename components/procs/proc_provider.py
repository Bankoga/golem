from utils.object_factory import *
from data.axioms.configs import proc_ids
from components.procs.glg import GLGBuilder
from components.procs.dc_granular_cort import DCGranularCortBuilder
from components.procs.df_granular_cort import DFGranularCortBuilder
from components.procs.dc_agranular_cort import DCAgranularCortBuilder
from components.procs.df_agranular_cort import DFAgranularCortBuilder
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
proc_services.register_builder(proc_ids['dcgc'], DCGranularCortBuilder())
proc_services.register_builder(proc_ids['dfgc'], DFGranularCortBuilder())
proc_services.register_builder(proc_ids['dcagc'], DCAgranularCortBuilder())
proc_services.register_builder(proc_ids['dfagc'], DFAgranularCortBuilder())
# proc_services.register_builder(proc_ids['?'], ?Builder())
# proc_services.register_builder(proc_ids['?'], ?Builder())