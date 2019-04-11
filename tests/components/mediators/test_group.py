import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array_equal

from components.axioms.cell_types import CellType
from components.cogs.cells.cell import Cell
from components.enums.module import ModuleType
from components.enums.pos import CtgType
from components.enums.prop_types import GroupType, RsrcType
from components.matrix.channel_registry import ChannelRegistry
from components.matrix.lineage_registry import LineageRegistry
from components.mediators.group import Group
from components.vars.data import Lineage
from tests.components.base.mechanisms.test_mechanism import TestMechanism


class TestGroup(TestMechanism):
  def set_up_base(self):
    self.label = 'noise_dwn_inhib'
    self.ctg = CtgType.GROUP
    self.comp_class = Group

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_lineage_registry_api')
    self.lineage_registry = self.registry
    self.lineage = Lineage(golem='arith_brain',matrix='left',module='thalamus', stage='noise_ctrl',group=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.group_type = GroupType.ORGANO
    self.pct_of_stage = -1
    self.nodes_details = [
      {
        'node_type': CellType.PLATE,
        'pct_of_group': 1,
        'resources_accepted': [RsrcType.ENERGIZER,RsrcType.INHIBITOR]
      }
    ]
    self.source_index = (0,0)
    self.source_shape = (256,256)
    self.values = [self.registry,self.group_type,self.pct_of_stage,self.nodes_details]
    self.var = tuple(self.values)
    self.baseline = self.values
    
  def set_up_build_results(self):
    self.node_labels = [
      f'{self.label}_some_childlabel'
    ]
    self.nodes = [
      {
        'node': Cell(self.registry,
                    CellType.PLATE,
                    [RsrcType.ENERGIZER,RsrcType.INHIBITOR],
                    self.source_index,
                    self.source_shape,
                    label=self.node_labels[0]),
        'pct_of_group': 1
      }
    ]

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.set_up_build_results()
    self.comp = self.comp_class(*self.values,label=self.label)

  def test_get_group_type(self):
    self.assertEqual(self.comp.group_type, self.group_type)
  def test_set_group_type(self):
    with self.assertRaises(RuntimeError):
      self.comp.group_type = self.group_type
  
  def test_get_pct_of_stage(self):
    self.assertEqual(self.comp.pct_of_stage, self.pct_of_stage)
  def test_set_pct_of_stage(self):
    with self.assertRaises(RuntimeError):
      self.comp.pct_of_stage = self.pct_of_stage

  def test_get_nodes_details(self):
    self.assertTrue(array_equal(self.comp.nodes_details, self.nodes_details))
  def test_set_nodes_details(self):
    with self.assertRaises(RuntimeError):
      self.comp.nodes_details = self.nodes_details

  def test_create_nodes(self):
    res = self.comp.create_nodes(self.nodes_details)
    self.assertEqual(len(res), len(self.nodes_details))
    self.assertEqual(res, self.nodes)

  def test_create_arb_nodes(self,nodes_details):
    res = self.comp.create_nodes(nodes_details)
    nodes = [{}]
    self.assertEqual(len(res), len(nodes_details))
    self.assertEqual(res, nodes)

if __name__ == '__main__':
  unittest.main()
