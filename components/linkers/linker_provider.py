from utils.object_factory import *
from data.axioms.configs import links
from linkers.loop_i import LoopILinkerBuilder
from linkers.dm import DmLinkerBuilder
from linkers.gate_i import GateILinkerBuilder
from linkers.synch_i import SynchILinkerBuilder
from linkers.synch_all import SynchAllLinkerBuilder

class LinkerProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, linker_id, **kwargs):
    return self.create(linker_id, **kwargs)

services = LinkerProvider()
services.register_builder('loop_i', LoopILinkerBuilder())
services.register_builder('dm', DmLinkerBuilder())
services.register_builder('gate_i', GateILinkerBuilder())
services.register_builder('synch_i', SynchILinkerBuilder())
services.register_builder('synch_all', SynchAllLinkerBuilder())