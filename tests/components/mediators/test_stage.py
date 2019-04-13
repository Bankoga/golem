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
from components.mediators.stage import Stage
from components.vars.data import Lineage
from tests.components.base.mechanisms.test_mechanism import TestMechanism


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
        'id': 'noise_dwn_inhib',
        'group_type': GroupType.ORGANO,
        'node_details': [
          {
            'node_type': CellType.PLATE,
            'pct_of_group': 1,
            'resources_accepted': [RsrcType.ENERGIZER,RsrcType.INHIBITOR]
          }
        ],
        'pct_of_stage': -1
      },
      {
        'id': 'noise_adj_inhib',
        'group_type': GroupType.ORGANO,
        'node_details': [
          {
            'node_type': CellType.PLATE,
            'pct_of_group': 1,
            'resources_accepted': [RsrcType.ENERGIZER,RsrcType.INHIBITOR]
          }
        ],
        'pct_of_stage': -1
      }
    ]
    self.shape = (256,256)
    self.values = [self.registry,self.shape,self.group_defs]
    self.var = tuple(self.values)
    self.baseline = self.values
    
  # def set_up_build_results(self):
  #   self.node_labels = [
  #     f'{self.label}_some_childlabel'
  #   ]
  #   self.groups = [
  #     Group(
  #       group_type: ORGANO
  #       node_details:
  #         - node_type: plate
  #           pct_of_group: 1
  #       pct_of_stage: -1
  #       label = 'noise_dwn_inhib'
  #     ),
  #   Group(
  #       group_type: ORGANO
  #       node_details:
  #         - node_type: plate
  #           pct_of_group: 1
  #       pct_of_stage: -1
  #       label='noise_adj_inhib'
  #   )
  #   ]

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    # self.set_up_build_results()
    self.comp = self.comp_class(*self.values,label=self.label)

    # [self.registry,
    #  self.group_type,
    #  self.source_index,
    #  self.source_shape,
    #  self.pct_of_stage,
    #  self.nodes_details]

if __name__ == '__main__':
  unittest.main()
