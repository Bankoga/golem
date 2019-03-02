from utils.object_factory import *
from utils.cardinators.asc_cardinator import AscCardinatorBuilder
from utils.cardinators.dsc_cardinator import DscCardinatorBuilder
# from components.hooks.gate_i import GateILinkerBuilder
# from components.hooks.synch_i import SynchILinkerBuilder
# from components.hooks.synch_all import SynchAllLinkerBuilder

class CardinatorProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, cardinator_id, **kwargs):
    return self.create(cardinator_id, **kwargs)

cardinator_services = CardinatorProvider()
cardinator_services.register_builder('asc', AscCardinatorBuilder())
cardinator_services.register_builder('dsc', DscCardinatorBuilder())
# cardinator_services.register_builder('dm', DmLinkerBuilder())
# cardinator_services.register_builder('gate_i', GateILinkerBuilder())
# cardinator_services.register_builder('synch_i', SynchILinkerBuilder())
# cardinator_services.register_builder('synch_all', SynchAllLinkerBuilder())