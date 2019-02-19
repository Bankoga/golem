from utils.object_factory import *
from data.axioms.configs import coder_ids
from components.coders.parts_sensor import PartsSensorBuilder
# from components.coders.dc_granular_cort import DCGranularCortBuilder

class CoderProvider(ObjectFactory):
  """
  The factory responsible for handling each type of supported link between modules
  """
  def get(self, coder_id, **kwargs):
    return self.create(coder_id, **kwargs)

coder_services = CoderProvider()
coder_services.register_builder(coder_ids['ps'], PartsSensorBuilder())
# coder_services.register_builder(coder_ids['?'], ?Builder())
# coder_services.register_builder(coder_ids['?'], ?Builder())