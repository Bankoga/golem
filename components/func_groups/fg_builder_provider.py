from data.enums.prop_types import GroupType
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
    parts = fg_type_id.split('-')
    if parts[0] is GroupType.SENSOR:
      # then use the prexisting sensor Builder
      pass
    elif parts[0] is GroupType.CORTICAL or parts[0] is GroupType.GATEWAY:
      # then use the procs Builder
      pass
    else:
      raise ValueError('The id does not indicate a valid thing!')

    return self.create(fg_type_id, **kwargs)

fg_services = FGBuilderProvider()
# fg_services.register_builder('', Builder())
# fg_services.register_builder('', Builder())
# fg_services.register_builder('', Builder())
# fg_services.register_builder('', Builder())
# fg_services.register_builder('', Builder())
# fg_services.register_builder('', Builder())