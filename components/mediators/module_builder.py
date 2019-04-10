from components.enums.prop_types import ModuleType
from utils.object_factory import *
# # from components.mediators.asc_cardinator import AscCardinatorBuilder
# # from components.mediators.dsc_cardinator import DscCardinatorBuilder
# # from components.hooks.gate_i import GateILinkerBuilder
# # from components.hooks.synch_i import SynchILinkerBuilder
# # from components.hooks.synch_all import SynchAllLinkerBuilder

# class ModuleBuilder(ObjectFactory):
#   """
#   The factory responsible for handling each type of supported link between modules
#   """
#   def get(self, fs_type_id, **kwargs):
#     parts = fs_type_id.split('-')
#     if parts[0] is ModuleType.SENSOR:
#       # then use the prexisting sensor Builder
#       pass
#     elif parts[0] is ModuleType.CORTICAL or parts[0] is ModuleType.GATEWAY:
#       # then use the procs Builder
#       pass
#     else:
#       raise ValueError('The id does not indicate a valid thing!')

#     return self.create(fs_type_id, **kwargs)

# # fs_services.register_builder('', Builder())
# # fs_services.register_builder('', Builder())
# # fs_services.register_builder('', Builder())
# # fs_services.register_builder('', Builder())
# # fs_services.register_builder('', Builder())
# # fs_services.register_builder('', Builder())

from components.enums.prop_types import ModuleType, SuperSet
from utils.object_factory import *
from components.mediators.coders.coder_provider import coder_services
from components.mediators.procs.proc_provider import proc_services
from components.mediators.coders.coder import Coder
from components.mediators.procs.proc import Proc
from components.mediators.module import Module

class ModuleBuilder(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, fs_type_id, **kwargs):
    if fs_type_id is None:
      raise ValueError('Invalid paramater value')
    parts = fs_type_id.split('-')
    fs_type = SuperSet[parts[0].split('.')[1]]
    # if 100 < parts[0].value and parts[0].value < 200:
    if fs_type is None:
      raise ValueError('Invalid group type')
    if fs_type is SuperSet.CODER:
      return coder_services.get(parts[1])
    # elif 200 < fs_type.value and fs_type.value < 300:
    elif fs_type is SuperSet.PROC:
      return proc_services.get(parts[1])
    # elif fs_type.value > 1:
    #   return self.create(fs_type_id, **kwargs)
    else:
      raise ValueError('The id does not indicate a valid thing!')


fs_services = ModuleBuilder()