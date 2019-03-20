import typing

from components.enums.prop_types import RsrcType,ChannelType
from components.vars.data import Address

class Meld(typing.NamedTuple):
  ch_type: ChannelType = ChannelType.OVERLAY
  resource: RsrcType = RsrcType.ENERGY
  address: Address = None
  shape: tuple = (1,1)

def read_meld_str(meld_str):
  meld_tuple = meld_str.split(';')
  return Meld(*meld_tuple)