from components.base.mechanisms.mediators.mediator import Mediator
from components.enums.pos import CtgType
from components.enums.prop_types import ChannelType,RsrcType
from chainer import Variable
from components.vars.meld import read_meld_str
from components.vars.data import Address

class Channel(Mediator):
  """
  For all intents and purposes, a package is a mail package
  It has the following properties
    - sender
    - recipient
    - type
    - shape : valid field type TODO: revisit shape
    - var : chainer variable
  there are two types of data packs planned currently
  - overlayed
    - is to be processed by itself as a full shape
  - aggregated
    - gets joined with others using a guaranteed ordering to produce a full shape to be processed
  
  eventually, are package shapes going to be chainer variables?
  """
  def __init__(self, meld_str,sender_address, **kwargs):
    # meld_var = read_meld_str(meld)
    args = [{},{},meld_str,sender_address]
    kwargs['ctg'] = CtgType.CHANNEL
    super().__init__(*args,**kwargs)
    self.__meld = None

  @property
  def reg_item(self):
    return {
      'reg_id': self.label,
      'recipient': self.recipient,
      'sender': self.sender
    }

  @property
  def address_registry(self):
    return self.var[1]

  @address_registry.setter
  def address_registry(self, value):
    raise RuntimeError('Cannot set address registry!')

  @property
  def channel_registry(self):
    return self.registry

  @channel_registry.setter
  def channel_registry(self, value):
    raise RuntimeError('Cannot set channel registry!')

  @reg_item.setter
  def reg_item(self, value):
    raise RuntimeError('The reg item cannot be set!')
  
  @property
  def meld_str(self):
    return self.var[2]
  
  @meld_str.setter
  def meld_str(self, value):
    self.setter_error()
    
  @property
  def meld(self):
    if self.__meld is None:
      self.__meld = read_meld_str(self.meld_str)
    else:
      return self.__meld
  
  @meld.setter
  def meld(self, value):
    self.setter_error()

  @property
  def recipient(self):
    return self.meld.address

  @recipient.setter
  def recipient(self, value):
    self.setter_error()

  @property
  def sender(self):
    return self.var[3]

  @sender.setter
  def sender(self, value):
    self.setter_error()

  @property
  def shape(self):
    return self.meld.shape

  @shape.setter
  def shape(self, value):
    self.setter_error()

  @property
  def resource(self):
    return RsrcType[self.meld.resource]

  @resource.setter
  def resource(self, value):
    self.setter_error()

  @property
  def ch_type(self):
    return ChannelType[self.meld.ch_type]

  @ch_type.setter
  def ch_type(self, value):
    self.setter_error()
    
  def build_details(self, *args, **kwargs):
    self.__meld = read_meld_str(self.meld_str)
    if 'address' in kwargs:
      self.register(kwargs['address'])