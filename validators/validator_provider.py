from utils.object_factory import *
from data.axioms.configs import proc_types, procs, links
# from validators.loop_i import LoopILinkerBuilder
# from validators.dm import DmLinkerBuilder
# from validators.gate_i import GateILinkerBuilder
# from validators.synch_i import SynchILinkerBuilder
# from validators.synch_all import SynchAllLinkerBuilder

class ValidatorProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, linker_id, **kwargs):
    return self.create(linker_id, **kwargs)

services = ValidatorProvider()
# proc validators - 1 per proc
# services.register_builder('DCLEG', DCLEGBuilder())
# services.register_builder('DFLEG', DFLEGBuilder())
# services.register_builder('GLG', GLGBuilder())
# services.register_builder('PICG', PICGBuilder())
# services.register_builder('POCG', POCGBuilder())
# services.register_builder('TICG', TICGBuilder())
# 'ASLG'
# 'SLG'
# 'MLG'
# 'KBLG'

# proc type validators - 1 per proc type?

# golem validator - 2
# services.register_builder('golem_config', POCGBuilder())
# services.register_builder('golem_full', TICGBuilder())

# link validators - 1 per link or link type?

# 