import unittest

import hypothesis.strategies as st
from hypothesis import given
from numpy import array_equal

from components.axioms.props import dest_key_pattern
from components.enums.prop_types import FieldType, ChannelType, ResourceType
from components.channels.misc_funcs import (build_lineage, build_meld,
                                            build_package,
                                            build_channel_inputs)
from components.enums.pos import CtgType
from components.channels.channel import Channel
from components.vars.data import Lineage
from components.matrix.lineage_registry import LineageRegistry
from components.matrix.channel_registry import ChannelRegistry
from components.vars.meld import read_meld_str
from tests.components.base.mechanisms.mediators.test_mediator import TestMediator
from tests.strategies.channel_strats import arb_meld_str
from tests.strategies.data_strats import valid_resource_data
from tests.strategies.channel_strats import (channel_arbitrary, channel_inputs,
                                             valid_channel_arbitrary)
from tests.strategies.pos_strats import arb_lineage

class TestChannel(TestMediator):
  def set_up_base(self):
    self.label = 'ch_bc_star_energy'
    self.ctg = CtgType.CHANNEL
    self.comp_class = Channel

  def set_up_var(self):
    self.lineage_registry = LineageRegistry(label='global_lineage_registry_api')
    self.registry = ChannelRegistry(label='global_channel_registry_api')
    self.channel_registry = self.registry
    self.sender = Lineage(golem='a',matrix='l',module='glg', stage='prim', group='assoc_from')
    self.lineage = None
    self.recipient = Lineage(golem='a',matrix='l',module='vis_a')
    self.shape = tuple([256,256])
    self.resource = ResourceType.ENERGIZER
    self.ch_type = ChannelType.AGGREGATE
    self.meld_str = f'{self.ch_type.name};{self.resource.name};{self.recipient};{self.shape}'
    self.meld_var = read_meld_str(self.meld_str)
    self.reg_item = {
      'reg_id': self.label,
      'recipient': str(self.recipient),
      'sender': str(self.sender)
    }
    self.values = [self.registry,self.lineage_registry,str(self.meld_var),str(self.sender)]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = self.comp_class(self.meld_str,self.sender,label=self.label, ctg=self.ctg)
    self.comp.update(*self.values)

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

  def test_update(self):
    # self.comp = self.comp_class(self.meld_str,self.sender,label=self.label, ctg=self.ctg)
    meld_str = f'{self.ch_type.name};{self.resource.name};{self.sender};{self.shape}'
    meld_var = read_meld_str(meld_str)
    self.values[2] = str(meld_var)
    self.comp.update(*self.values)
    self.assertEqual(self.comp.meld,meld_var)
    self.assertEqual(self.comp.var, tuple(self.values))
  
  
  # TODO: rewrite to lineage diff between channel registry and lineage registry when going over connections later
  # @given(st.one_of(lineage_reg(), st.integers())) # pylint: disable=no-value-for-parameter
  # def test_set_registry(self, possible_reg):
  #   if type(possible_reg) == LineageRegistry:
  #     self.comp.registry = possible_reg
  #     self.assertEqual(self.comp.registry, possible_reg)
  #   else:
  #     with self.assertRaises(RuntimeError):
  #       self.comp.registry = possible_reg

if __name__ == '__main__':
    unittest.main()
