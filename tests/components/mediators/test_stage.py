import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array_equal

from components.axioms.cell_types import CellType
from components.cogs.cells.cell import Cell
from components.enums.module import ModuleType
from components.enums.pos import CtgType
from components.enums.prop_types import GroupType, ResourceType
from components.matrix.channel_registry import ChannelRegistry
from components.matrix.lineage_registry import LineageRegistry
from components.mediators.group import Group
from components.mediators.stage import Stage
from components.vars.data import Lineage
from tests.components.base.mechanisms.test_mechanism import TestMechanism
from utils.helpers.arrayer import get_sizes
from tests.strategies.module_strats import arb_group_def

class TestStage(TestMechanism):
  def set_up_base(self):
    self.label = 'noise_ctrl'
    self.ctg = CtgType.STAGE
    self.comp_class = Stage

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_lineage_registry_api')
    self.lineage_registry = self.registry
    self.lineage = Lineage(golem='arith_brain',matrix='left',module='thalamus', stage=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.group_defs = [
      {
        'label': 'noise_dwn_inhib',
        'group_type': GroupType.ORGANO,
        'node_details': [
          {
            'node_type': CellType.PLATE,
            'pct_of_group': 1,
            'resources_accepted': [ResourceType.ENERGIZER,ResourceType.INHIBITOR]
          }
        ],
        'pct_of_stage': -1
      },
      {
        'label': 'noise_adj_inhib',
        'group_type': GroupType.ORGANO,
        'node_details': [
          {
            'node_type': CellType.PLATE,
            'pct_of_group': 1,
            'resources_accepted': [ResourceType.ENERGIZER,ResourceType.INHIBITOR]
          }
        ],
        'pct_of_stage': -1
      }
    ]
    self.shape = (16,16)
    self.values = [self.registry,self.shape,self.group_defs]
    self.var = tuple(self.values)
    
  # def set_up_build_results(self):
  #   groups = []

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    # self.set_up_build_results()
    self.comp = self.comp_class(*self.values,label=self.label)

  def test_get_shape(self):
    self.assertEqual(self.comp.shape, self.shape)
  def test_set_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.shape = self.shape
  
  def test_get_group_defs(self):
    self.assertEqual(self.comp.group_defs, self.group_defs)
  def test_set_group_defs(self):
    with self.assertRaises(RuntimeError):
      self.comp.group_defs = self.group_defs

  def layer_check(self, group_def, res):
    x,y = get_sizes(self.shape)
    for row in range(x):
      for col in range(y):
        index = (row,col)
        group = Group(self.registry,
                      group_def['group_type'],
                      index,
                      self.shape,
                      group_def['pct_of_stage'],
                      group_def['node_details'],
                      label=f'{group_def["label"]}_{row}_{col}')
        self.assertIn(group, res)

  @given(arb_group_def()) # pylint: disable=no-value-for-parameter
  def test_create_layer(self, group_def):
    res = self.comp.create_layer(group_def)
    self.layer_check(group_def, res)

  def test_create_groups(self):
    res = self.comp.create_groups(self.group_defs)
    for group_def in self.group_defs:
      self.layer_check(group_def, res)
    # self.assertTrue(type(group) is Group
    #               and group.label == self.group_defs[i]['label']
    #               and group == self.groups[i] for i,group in enumerate(res))

if __name__ == '__main__':
  unittest.main()
