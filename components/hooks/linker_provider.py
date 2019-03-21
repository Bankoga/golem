from utils.object_factory import *
from components.axioms.configs import links
from components.hooks.loop_i import LoopILinkerBuilder
from components.hooks.dm import DmLinkerBuilder
from components.hooks.gate_i import GateILinkerBuilder
from components.hooks.synch_i import SynchILinkerBuilder
from components.hooks.synch_all import SynchAllLinkerBuilder

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