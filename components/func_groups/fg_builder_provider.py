from utils.object_factory import *
# from components.func_groups.asc_ordinator import AscOrdinatorBuilder
# from components.func_groups.dsc_ordinator import DscOrdinatorBuilder
# from components.linkers.gate_i import GateILinkerBuilder
# from components.linkers.synch_i import SynchILinkerBuilder
# from components.linkers.synch_all import SynchAllLinkerBuilder

class FGBuilderProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, fg_type_id, **kwargs):
    return self.create(fg_type_id, **kwargs)

fg_services = FGBuilderProvider()
# fg_services.register_builder('asc', AscOrdinatorBuilder())
# fg_services.register_builder('dsc', DscOrdinatorBuilder())
# fg_services.register_builder('dm', DmLinkerBuilder())
# fg_services.register_builder('gate_i', GateILinkerBuilder())
# fg_services.register_builder('synch_i', SynchILinkerBuilder())
# fg_services.register_builder('synch_all', SynchAllLinkerBuilder())