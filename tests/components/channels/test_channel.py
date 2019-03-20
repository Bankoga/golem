import unittest

import hypothesis.strategies as st
from hypothesis import given
from numpy import array_equal

from components.axioms.props import dest_key_pattern
from components.enums.prop_types import FieldType, ChannelType, RsrcType
from components.channels.misc_funcs import (build_address, build_meld,
                                            build_package,
                                            build_channel_inputs)
from components.enums.pos import CtgType
from components.channels.channel import Channel
from components.vars.data import Address
from components.matrix.address_registry import AddressRegistry
from components.matrix.channel_registry import ChannelRegistry
from components.vars.meld import read_meld_str
from tests.components.base.workers.test_mediator_comp import TestMediatorComp
from tests.strategies.channel_strats import arb_meld_str
from tests.strategies.data_strats import valid_resource_data
from tests.strategies.channel_strats import (channel_arbitrary, channel_inputs,
                                             valid_channel_arbitrary)
from tests.strategies.pos_strats import arb_addr

class TestChannel(TestMediatorComp):
  def setUp(self):
    self.address_registry = AddressRegistry(label='global_address_registry_api')
    self.channel_registry = ChannelRegistry(label='global_channel_registry_api')
    self.address = Address(golem='a',matrix='l',func_set='glg', group='assoc_from')
    self.recipient = Address(golem='a',matrix='l',func_set='vis_a')
    self.shape = (256,256)
    self.resource = RsrcType.ENERGY
    self.channel_type = ChannelType.AGGREGATE
    self.meld_str = f'{self.recipient};{self.resource};{self.channel_type};{self.shape}'
    self.meld_var = read_meld_str(self.meld_str)
    self.label = 'ch_bc_star_energy'
    self.ctg = CtgType.CHANNEL
    self.reg_item = {
      'reg_id': self.label,
      'recipient': self.recipient,
      'sender': self.address
    }
    self.values = [self.address_registry,self.channel_registry,self.meld_var,self.address]
    self.var = tuple(self.values)
    self.comp = Channel(self.meld_str,self.address,label=self.label, ctg=self.ctg)

  @given(arb_meld_str(), arb_addr()) # pylint: disable=no-value-for-parameter
  def test_get_args(self, meld_str,sender_address):
    meld_var = read_meld_str(self.meld_str)
    result = self.comp.get_args(meld_var,sender_address)
    expectation = [{},{},meld_var,sender_address]
    self.assertEqual(result,expectation)

if __name__ == '__main__':
    unittest.main()
