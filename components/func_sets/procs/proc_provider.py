from utils.object_factory import *
from data.axioms.configs import proc_ids
from components.func_sets.procs.glg import GLGBuilder
from components.func_sets.procs.dc_granular_cort import DCGranularCortBuilder
from components.func_sets.procs.df_granular_cort import DFGranularCortBuilder
from components.func_sets.procs.dc_agranular_cort import DCAgranularCortBuilder
from components.func_sets.procs.df_agranular_cort import DFAgranularCortBuilder
# from components.func_sets.procs.synch_i import SynchILinkerBuilder
# from components.func_sets.procs.synch_all import SynchAllLinkerBuilder

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