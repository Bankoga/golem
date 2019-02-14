from utils.object_factory import *
from data.axioms.configs import links
from utils.linkers.loop_i import LoopILinkerBuilder
from utils.linkers.dm import DmLinkerBuilder
from utils.linkers.gate_i import GateILinkerBuilder
from utils.linkers.synch_i import SynchILinkerBuilder
from utils.linkers.synch_all import SynchAllLinkerBuilder

class LinkerProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, linker_id, **kwargs):
    return self.create(linker_id, **kwargs)

linkers = LinkerProvider()
linkers.register_builder('loop_i', LoopILinkerBuilder())
linkers.register_builder('dm', DmLinkerBuilder())
linkers.register_builder('gate_i', GateILinkerBuilder())
linkers.register_builder('synch_i', SynchILinkerBuilder())
linkers.register_builder('synch_all', SynchAllLinkerBuilder())