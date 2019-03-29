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