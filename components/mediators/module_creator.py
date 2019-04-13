from components.enums.prop_types import ModuleType
from utils.object_factory import *
# # from components.mediators.asc_cardinator import AscCardinatorBuilder
# # from components.mediators.dsc_cardinator import DscCardinatorBuilder
# # from components.hooks.gate_i import GateILinkerBuilder
# # from components.hooks.synch_i import SynchILinkerBuilder
# # from components.hooks.synch_all import SynchAllLinkerBuilder

# class ModuleCreator(ObjectFactory):
#   """
#   The factory responsible for handling each type of supported link between modules
#   """
#   def get(self, module_type_id, **kwargs):
#     parts = module_type_id.split('-')
#     if parts[0] is ModuleType.SENSOR:
#       # then use the prexisting sensor Builder
#       pass
#     elif parts[0] is ModuleType.CORTICAL or parts[0] is ModuleType.GATEWAY:
#       # then use the procs Builder
#       pass
#     else:
#       raise ValueError('The id does not indicate a valid thing!')

#     return self.create(module_type_id, **kwargs)

# # module_creator_services.register_builder('', Builder())
# # module_creator_services.register_builder('', Builder())
# # module_creator_services.register_builder('', Builder())
# # module_creator_services.register_builder('', Builder())
# # module_creator_services.register_builder('', Builder())
# # module_creator_services.register_builder('', Builder())

from components.enums.prop_types import ModuleType, SuperSet
from utils.object_factory import *
from components.mediators.coders.coder_provider import coder_services
from components.mediators.procs.proc_provider import proc_services
from components.mediators.coders.coder import Coder
from components.mediators.procs.proc import Proc
from components.mediators.module import Module

class ModuleCreator(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, module_type_id, **kwargs):
    if module_type_id is None:
      raise ValueError('Invalid paramater value')
    parts = module_type_id.split('-')
    module_type = SuperSet[parts[0].split('.')[1]]
    # if 100 < parts[0].value and parts[0].value < 200:
    if module_type is None:
      raise ValueError('Invalid group type')
    if module_type is SuperSet.CODER:
      return coder_services.get(parts[1])
    # elif 200 < module_type.value and module_type.value < 300:
    elif module_type is SuperSet.PROC:
      return proc_services.get(parts[1])
    # elif module_type.value > 1:
    #   return self.create(module_type_id, **kwargs)
    else:
      raise ValueError('The id does not indicate a valid thing!')


module_creator_services = ModuleCreator()