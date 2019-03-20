from components.base.workers.mediator_comp import MediatorComp
from components.enums.pos import CtgType
from components.enums.prop_types import ChannelType,RsrcType,FieldType
from chainer import Variable

class Channel(MediatorComp):
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
  def __init__(self, meld,sender_address, **kwargs):
    args = self.read_meld(meld,sender_address)
    kwargs['ctg'] = CtgType.CHANNEL
    super().__init__(*args,**kwargs)
  
  def read_meld(self, meld,sender_address):
    meld_tuple = meld.split(';')
    recipient=meld_tuple[0]
    resource=RsrcType.UNSET
    shape = (-1,-1)
    channel_type = ChannelType.UNSET
    if len(meld_tuple) > 1 and meld_tuple[1] and meld_tuple[1] in RsrcType:
      resource = meld_tuple[1]
      if meld_tuple[2] != 0 and meld_tuple[2] in ChannelType:
        channel_type=ChannelType(meld_tuple[2])
        if len(meld_tuple) >3 and meld_tuple[3] and type(meld_tuple[3]) == tuple:
          shape=meld_tuple[3]
    return [{},{},channel_type,meld,recipient,resource,sender_address,shape]

  # def get_meld(self):
  #     return f'{self.sender};{self.recipient};{self.resource};{self.channel_type};{self.shape}'

  # def update(self, new_addr):
  #   self.recipient = new_addr
  #   self._built_ = False
  #   self.var = None