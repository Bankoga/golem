from components.base.mechanisms.mechanism import Mechanism

class Mediator(Mechanism):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  @property
  def address_registry(self):
    return self.registry

  @address_registry.setter
  def address_registry(self, value):
    raise RuntimeError('Cannot set address registry!')

  @property
  def channel_registry(self):
    return self.var[1]

  @channel_registry.setter
  def channel_registry(self, value):
    raise RuntimeError('Cannot set channel registry!')
  
  # def collect_relative_addresses():
  # for each read, we change the Z in the direction supplied using the PROPER cardinator
  #  we also change the size of the sample
  #   this means we either have to be given the cardinator
  #   OR
  #   we have to be able to select the cardinator
  #   so that we can get_card_index(ind, inputs)
  #   context.get_inputs_at_steps_in(direction, inputs)
  #   input_pack = select the inputs using our Pos info plus the card index
  
  # @given(processed_module_input_set()) # pylint: disable=no-value-for-parameter
  # def test_operate(self, inputs):
  #   """
  #   At a cell level, we execute all of our instructions using a method provided by the context
  #   At an instruction level, we execute on the inputs within context in the direction specified using the contextual cardinator
  #   for each direction
  #     take a sample of the package shape for each shape
  #     record activity information while sampling
  #   combine all samples into a single result using distance attenuation
  #   """
  #   packages = inputs[0]
  #   fs = inputs[1]
  #   result = self.comp.operate(packages,fs)
  #   parts = []
  #   # for pack in inputs:
  #   # for each instruction
  #   #   we grab specifed_input from the inputs
  #   #   we apply a 2d convolution with the specified shape
  #   #   we do what with the result?