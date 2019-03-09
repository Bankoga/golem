from data.enums.prop_types import FuncSetType
from utils.object_factory import *
# # from components.func_sets.asc_cardinator import AscCardinatorBuilder
# # from components.func_sets.dsc_cardinator import DscCardinatorBuilder
# # from components.hooks.gate_i import GateILinkerBuilder
# # from components.hooks.synch_i import SynchILinkerBuilder
# # from components.hooks.synch_all import SynchAllLinkerBuilder

# class FSBuilderProvider(ObjectFactory):
#   """
#   The factory responsible for handling each type of supported link between modules
#   """
#   def get(self, fs_type_id, **kwargs):
#     parts = fs_type_id.split('-')
#     if parts[0] is FuncSetType.SENSOR:
#       # then use the prexisting sensor Builder
#       pass
#     elif parts[0] is FuncSetType.CORTICAL or parts[0] is FuncSetType.GATEWAY:
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

from data.enums.prop_types import FuncSetType, SuperSet
from utils.object_factory import *
from components.func_sets.coders.coder_provider import coder_services
from components.func_sets.procs.proc_provider import proc_services
from components.func_sets.coders.coder import Coder
from components.func_sets.procs.proc import Proc
from components.func_sets.func_set import FuncSet
from components.component import Component

class FSBuilderProvider(ObjectFactory):
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


fs_services = FSBuilderProvider()