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
from tests.components.base.mechanisms.test_mediator import TestMediator
from tests.strategies.channel_strats import arb_meld_str
from tests.strategies.data_strats import valid_resource_data
from tests.strategies.channel_strats import (channel_arbitrary, channel_inputs,
                                             valid_channel_arbitrary)
from tests.strategies.pos_strats import arb_addr

class TestChannel(TestMediator):
  def set_up_base(self):
    self.label = 'ch_bc_star_energy'
    self.ctg = CtgType.CHANNEL

  def set_up_var(self):
    self.address_registry = AddressRegistry(label='global_address_registry_api')
    self.registry = ChannelRegistry(label='global_channel_registry_api')
    self.channel_registry = self.registry
    self.sender = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from')
    self.address = None
    self.recipient = Address(golem='a',matrix='l',func_set='vis_a')
    self.shape = tuple([256,256])
    self.resource = RsrcType.ENERGY
    self.ch_type = ChannelType.AGGREGATE
    self.meld_str = f'{self.ch_type.name};{self.resource.name};{self.recipient};{self.shape}'
    self.meld_var = read_meld_str(self.meld_str)
    self.reg_item = {
      'reg_id': self.label,
      'recipient': str(self.recipient),
      'sender': str(self.sender)
    }
    self.values = [self.registry,self.address_registry,str(self.meld_var),str(self.sender)]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = Channel(self.meld_str,self.sender,label=self.label, ctg=self.ctg)
    self.comp.build(*self.values)

  def test_get_meld_str(self):
    self.assertEqual(self.comp.meld_str, self.meld_str)

  def test_set_meld_str(self):
    with self.assertRaises(RuntimeError):
      self.comp.meld_str  = 'Some string'

  def test_get_meld(self):
    self.assertEqual(self.comp.meld, self.meld_var)

  def test_set_meld(self):
    with self.assertRaises(RuntimeError):
      self.comp.meld  = 'Some string'

  def test_get_recipient(self):
    self.assertEqual(self.comp.recipient, str(self.recipient))

  def test_set_recipient(self):
    with self.assertRaises(RuntimeError):
      self.comp.recipient  = 'Some string'

  def test_get_sender(self):
    self.assertEqual(self.comp.sender, str(self.sender))

  def test_set_sender(self):
    with self.assertRaises(RuntimeError):
      self.comp.sender  = 'Some string'

  def test_get_shape(self):
    self.assertEqual(self.comp.shape, self.shape)

  def test_set_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.shape  = (94,40)

  def test_get_resource(self):
    self.assertEqual(self.comp.resource, self.resource)

  def test_set_resource(self):
    with self.assertRaises(RuntimeError):
      self.comp.resource  = 'Some string'

  def test_get_ch_type(self):
    self.assertEqual(self.comp.ch_type, self.ch_type)

  def test_set_ch_type(self):
    with self.assertRaises(RuntimeError):
      self.comp.ch_type  = 'Some string'

  def test_build_with_data(self):
    self.comp = Channel(self.meld_str,self.sender,label=self.label, ctg=self.ctg)
    meld_str = f'{self.ch_type.name};{self.resource.name};{self.sender};{self.shape}'
    meld_var = read_meld_str(meld_str)
    self.values[2] = str(meld_var)
    self.comp.build(*self.values)
    self.assertEqual(self.comp.meld,meld_var)
    self.assertEqual(self.comp.var, tuple(self.values))
    self.assertTrue(self.comp.is_built)

if __name__ == '__main__':
    unittest.main()
