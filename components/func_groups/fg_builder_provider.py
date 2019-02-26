from utils.object_factory import *
# from components.func_groups.asc_cardinator import AscCardinatorBuilder
# from components.func_groups.dsc_cardinator import DscCardinatorBuilder
# from components.hooks.gate_i import GateILinkerBuilder
# from components.hooks.synch_i import SynchILinkerBuilder
# from components.hooks.synch_all import SynchAllLinkerBuilder

class FGBuilderProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, fg_type_id, **kwargs):
    return self.create(fg_type_id, **kwargs)

fg_services = FGBuilderProvider()
# fg_services.register_builder('asc', AscCardinatorBuilder())
# fg_services.register_builder('dsc', DscCardinatorBuilder())
# fg_services.register_builder('dm', DmLinkerBuilder())
# fg_services.register_builder('gate_i', GateILinkerBuilder())
# fg_services.register_builder('synch_i', SynchILinkerBuilder())
# fg_services.register_builder('synch_all', SynchAllLinkerBuilder())