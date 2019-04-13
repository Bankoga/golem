import typing

from components.enums.prop_types import ResourceType,ChannelType
from components.vars.data import Lineage

class Meld(typing.NamedTuple):
  ch_type: ChannelType = ChannelType.OVERLAY
  resource: ResourceType = ResourceType.ENERGIZER
  lineage: Lineage = None
  shape: tuple = (1,1)

  def __str__(self):
    return f'{self.ch_type};{self.resource};{self.lineage};{self.shape}'
  
  # TODO: add init to meld so that it can process string melds?

def read_meld_str(meld_str):
  meld_tuple = meld_str.split(';')
  return Meld(*meld_tuple)