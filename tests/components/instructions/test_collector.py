import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal

from components.data.collector_segment import CollectorSegment as cs
from components.enums.pos import CtgType
from components.enums.prop_types import RsrcType, RuleType
from components.instructions.collector import Collector
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from tests.components.instructions.test_instruction import TestInstruction
from tests.strategies.data_strats import (valid_resource_array,
                                          valid_resource_data, valid_shape,
                                          valid_shape_and_index,
                                          valid_sz_shape_and_index)
from tests.strategies.instruction_strats import (valid_collector_segment)
from tests.strategies.func_set_strats import (module_input_set,
                                              processed_module_input_set)
from tests.strategies.pos_strats import valid_direction, valid_pos
from tests.strategies.prop_strats import arb_label, rule_type_prop
from utils.helpers.prop_gen_help import roll_name
from utils.pos import Pos

class TestCollector(TestInstruction):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.INSTRUCTION
    self.rule_type= RuleType.CONV
    self.max_resources = 256
    self.comp_class = Collector
  
  def set_up_var(self):
    self.registry = AddressRegistry(label='global_address_registry_api')
    self.address = Address(golem='a',matrix='l',func_set='b', stage='a',group='a',packager='p',instruction=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.segment_defs = [
      (self.address,(4,4)),
      (self.address,(1,1)),
      (self.address,(4,4)),
      (self.address,(9,9),(1,1)),
      (self.address,(4,2),(1,1)),
      (self.address,(12,12))
    ]
    self.source_shape = (256,256)
    self.source_index = (45,25)
    self.step_direction = 'A' # TODO: Use correct ENUM
    self.num_steps = len(self.segment_defs)
    self.resource_accepted = RsrcType.ENERGY
    self.values = [self.registry,
                   self.source_index,
                   self.source_shape,
                   self.step_direction,
                   self.num_steps,
                   self.resource_accepted,
                   self.segment_defs
                  ]
    self.var = tuple(self.values)
    self.attenuation_rate = 2.5

  def set_up_dynamic_props(self):
    # self.pos = Pos(self.ctg.get_component_type())
    self.leaves = [cs(residence_address=self.address,source_address=self.address,source_index=self.source_index,fill_shape=(4,4),label=f'{self.label}_{roll_name()}'),
                        cs(residence_address=self.address,source_address=self.address,source_index=self.source_index,fill_shape=(1,1),label=f'{self.label}_{roll_name()}'),
                        cs(residence_address=self.address,source_address=self.address,source_index=self.source_index,fill_shape=(4,4),label=f'{self.label}_{roll_name()}'),
                        cs(residence_address=self.address,source_address=self.address,source_index=self.source_index,fill_shape=(9,9),label=f'{self.label}_{roll_name()}'),
                        cs(residence_address=self.address,source_address=self.address,source_index=self.source_index,fill_shape=(4,2),label=f'{self.label}_{roll_name()}'),
                        cs(residence_address=self.address,source_address=self.address,source_index=self.source_index,fill_shape=(12,12),label=f'{self.label}_{roll_name()}')]
    self.old_data = []
    self.prev_data = []

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.set_up_dynamic_props()
    self.comp = self.comp_class(self.registry,
                                self.source_index,
                                self.source_shape,
                                self.step_direction,
                                self.num_steps,
                                self.resource_accepted,
                                self.segment_defs,
                                label=self.label)
    self.comp.address = self.address

  def test_get_attenuation_rate(self):
    self.assertEqual(self.comp.attenuation_rate, self.attenuation_rate)
  def test_set_attenuation_rate(self):
    with self.assertRaises(RuntimeError):
      self.comp.attenuation_rate = self.attenuation_rate

  def test_get_source_ind(self):
    self.assertEqual(self.comp.source_index, self.source_index)
  def test_set_source_ind(self):
    with self.assertRaises(RuntimeError):
      self.comp.source_index = self.source_index
    
  def test_get_source_shape(self):
    self.assertEqual(self.comp.source_shape, self.source_shape)
  def test_set_source_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.source_shape = self.source_shape
    
  def test_get_step_direction(self):
    self.assertEqual(self.comp.step_direction, self.step_direction)
  def test_set_step_direction(self):
    with self.assertRaises(RuntimeError):
      self.comp.step_direction = self.step_direction
    
  def test_get_resource_accepted(self):
    self.assertEqual(self.comp.resource_accepted, self.resource_accepted)
  def test_set_resource_accepted(self):
    with self.assertRaises(RuntimeError):
      self.comp.resource_accepted = self.resource_accepted
    
  def test_get_collector_collector_defs(self):
    for i,cnv_shp in enumerate(self.comp.segment_defs):
      self.assertEqual(cnv_shp[0], self.segment_defs[i][0])
  def test_set_collector_collector_defs(self):
    with self.assertRaises(RuntimeError):
      self.comp.segment_defs = self.segment_defs

  @given(st.lists(valid_shape())) # pylint: disable=no-value-for-parameter
  def test_set_up_collector_segments(self,segment_defs):
    self.comp.set_up_collector_segments(segment_defs)
    for i,(addr,f_shape) in enumerate(segment_defs):
      self.assertTrue(self.comp.leaves[i].residence_address == addr)
      self.assertTrue(self.comp.leaves[i].fill_shape == f_shape)

  def test_get_leaves(self):
    for i,cllct_sgmnt in enumerate(self.comp.leaves):
      self.assertEqual(cllct_sgmnt.residence_address, self.leaves[i].residence_address)
      self.assertEqual(cllct_sgmnt.source_address, self.leaves[i].source_address)
      self.assertEqual(cllct_sgmnt.source_index, self.leaves[i].source_index)
      self.assertEqual(cllct_sgmnt.fill_shape, self.leaves[i].fill_shape)
  def test_set_leaves(self):
    with self.assertRaises(RuntimeError):
      self.comp.leaves = self.leaves

  @given(valid_resource_array()) # pylint: disable=no-value-for-parameter
  def test_instruction_details(self, npmatrix_array):
    results = self.comp.instruction_details(npmatrix_array)
    self.assertTrue(len(results),len(self.leaves))
    for i,item in enumerate(results):
      self.assertEqual(item.shape, self.comp.leaves[i].fill_shape)

if __name__ == '__main__':
  unittest.main()