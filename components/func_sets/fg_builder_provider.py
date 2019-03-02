from data.enums.prop_types import GroupType
from utils.object_factory import *
# # from components.func_sets.asc_cardinator import AscCardinatorBuilder
# # from components.func_sets.dsc_cardinator import DscCardinatorBuilder
# # from components.hooks.gate_i import GateILinkerBuilder
# # from components.hooks.synch_i import SynchILinkerBuilder
# # from components.hooks.synch_all import SynchAllLinkerBuilder

# class FGBuilderProvider(ObjectFactory):
#   """
#   The factory responsible for handling each type of supported link between modules
#   """
#   def get(self, fg_type_id, **kwargs):
#     parts = fg_type_id.split('-')
#     if parts[0] is GroupType.SENSOR:
#       # then use the prexisting sensor Builder
#       pass
#     elif parts[0] is GroupType.CORTICAL or parts[0] is GroupType.GATEWAY:
#       # then use the procs Builder
#       pass
#     else:
#       raise ValueError('The id does not indicate a valid thing!')

#     return self.create(fg_type_id, **kwargs)

# # fg_services.register_builder('', Builder())
# # fg_services.register_builder('', Builder())
# # fg_services.register_builder('', Builder())
# # fg_services.register_builder('', Builder())
# # fg_services.register_builder('', Builder())
# # fg_services.register_builder('', Builder())

from data.enums.prop_types import GroupType, SubGroup
from utils.object_factory import *
from components.func_sets.coders.coder_provider import coder_services
from components.func_sets.procs.proc_provider import proc_services
from components.func_sets.coders.coder import Coder
from components.func_sets.procs.proc import Proc
from components.func_sets.func_set import FuncGroup
from components.component import Component

class FGBuilderProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, fg_type_id, **kwargs):
    if fg_type_id is None:
      raise ValueError('Invalid paramater value')
    parts = fg_type_id.split('-')
    g_type = GroupType[parts[0].split('.')[1]]
    # if 100 < parts[0].value and parts[0].value < 200:
    if g_type is None:
      raise ValueError('Invalid group type')
    if g_type.sub_group() == SubGroup.CODER:
      return coder_services.get(parts[1])
    # elif 200 < g_type.value and g_type.value < 300:
    elif g_type.sub_group() == SubGroup.PROC:
      return proc_services.get(parts[1])
    # elif g_type.value > 1:
    #   return self.create(fg_type_id, **kwargs)
    else:
      raise ValueError('The id does not indicate a valid thing!')


fg_services = FGBuilderProvider()