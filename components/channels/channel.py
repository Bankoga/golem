from components.base.workers.mediator_comp import MediatorComp
from components.enums.pos import CtgType
from components.enums.prop_types import ChannelType,RsrcType,FieldType
from chainer import Variable
from components.vars.meld import read_meld_str

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
    meld_var = read_meld_str(meld)
    args = self.get_args(meld_var,sender_address)
    kwargs['ctg'] = CtgType.CHANNEL
    super().__init__(*args,**kwargs)
  
  def get_args(self, meld,sender_address):
    args = [{},{},meld,sender_address]
    # args.append(*meld)
    return args
    # return [{},{},channel_type,meld,recipient,resource,sender_address,shape]


  # def get_meld(self):
  #     return f'{self.sender};{self.recipient};{self.resource};{self.channel_type};{self.shape}'

  # def update(self, new_addr):
  #   self.recipient = new_addr
  #   self._built_ = False
  #   self.var = None