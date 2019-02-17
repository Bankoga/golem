from utils.object_factory import *
from components.ordinators.asc_ordinator import AscOrdinatorBuilder
from components.ordinators.dsc_ordinator import DscOrdinatorBuilder
# from components.linkers.gate_i import GateILinkerBuilder
# from components.linkers.synch_i import SynchILinkerBuilder
# from components.linkers.synch_all import SynchAllLinkerBuilder

class OrdinatorProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, ordinator_id, **kwargs):
    return self.create(ordinator_id, **kwargs)

ordinator_services = OrdinatorProvider()
ordinator_services.register_builder('asc', AscOrdinatorBuilder())
ordinator_services.register_builder('dsc', DscOrdinatorBuilder())
# ordinator_services.register_builder('dm', DmLinkerBuilder())
# ordinator_services.register_builder('gate_i', GateILinkerBuilder())
# ordinator_services.register_builder('synch_i', SynchILinkerBuilder())
# ordinator_services.register_builder('synch_all', SynchAllLinkerBuilder())