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
    self.registry = ChannelRegistry(label='global_channel_registry_api')
    self.sender = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from')
    self.address = None
    self.recipient = Address(golem='a',matrix='l',func_set='vis_a')
    self.shape = (256,256)
    self.resource = RsrcType.ENERGY
    self.ch_type = ChannelType.AGGREGATE
    self.meld_str = f'{self.ch_type.name};{self.resource.name};{self.recipient};{self.shape}'
    self.meld_var = read_meld_str(self.meld_str)
    self.label = 'ch_bc_star_energy'
    self.ctg = CtgType.CHANNEL
    self.reg_item = {
      'reg_id': self.label,
      'recipient': str(self.recipient),
      'sender': str(self.sender)
    }
    self.values = [self.registry,self.address_registry,self.meld_var,str(self.sender)]
    self.var = tuple(self.values)
    self.comp = Channel(self.meld_str,self.sender,label=self.label, ctg=self.ctg)

  @given(arb_meld_str(), arb_addr()) # pylint: disable=no-value-for-parameter
  def test_get_args(self, meld_str,sender_address):
    # TODO: EXPAND THE MELD FULLY FOR ARGS INSTEAD OF NESTING IT
    meld_var = read_meld_str(self.meld_str)
    result = self.comp.get_args(meld_var,sender_address)
    expectation = [{},{},meld_var,sender_address]
    self.assertEqual(result,expectation)

  def test_get_meld(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.meld, self.meld_var)

  def test_set_meld(self):
    with self.assertRaises(RuntimeError):
      self.comp.meld  = 'Some string'

  def test_get_recipient(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.recipient, str(self.recipient))

  def test_set_recipient(self):
    with self.assertRaises(RuntimeError):
      self.comp.recipient  = 'Some string'

  def test_get_sender(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.sender, str(self.sender))

  def test_set_sender(self):
    with self.assertRaises(RuntimeError):
      self.comp.sender  = 'Some string'

  def test_get_shape(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.shape, self.shape)

  def test_set_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.shape  = 'Some string'

  def test_get_resource(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.resource, self.resource)

  def test_set_resource(self):
    with self.assertRaises(RuntimeError):
      self.comp.resource  = 'Some string'

  def test_get_ch_type(self):
    self.comp.build(*self.values)
    self.assertEqual(self.comp.ch_type, self.ch_type)

  def test_set_ch_type(self):
    with self.assertRaises(RuntimeError):
      self.comp.ch_type  = 'Some string'

if __name__ == '__main__':
    unittest.main()
