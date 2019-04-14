import unittest

from hypothesis import given, reproduce_failure
from hypothesis import strategies as st
from numpy import append, array

from components.axioms.cell_types import CellType
from components.enums.pos import CtgType
from components.enums.prop_types import (ModuleType, SuperSet)
from components.matrix.channel_registry import ChannelRegistry
from components.matrix.lineage_registry import LineageRegistry
from components.mediators.module import Module
from components.vars.data import Lineage
from configs.procs.thalamus import group_defs, stage_defs, type_data
from tests.components.mediators.test_module import TestModule
from utils.cardinators.cardinator_provider import cardinator_services
from utils.misc import heapsort


class TestGLG(TestModule):
  def set_up_base(self):
    self.label = 'thalamus'
    self.ctg = CtgType.MODULE
    self.comp_class = Module

  def set_up_alt_props(self):
    self.shape = (16,16)

  def set_up_stages_defs(self):
    self.group_defs = group_defs
    self.stage_defs = stage_defs
    self.type_data = type_data

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_lineage_registry_api')
    self.channel_registry = ChannelRegistry(label='global_channel_registry_api')
    self.lineage_registry = self.registry
    self.lineage = Lineage(golem='a',matrix='l',module='glg')
    self.lineage = Lineage(golem='arith_brain',matrix='left',module=self.label)
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.module_type = ModuleType.GATEWAY
    self.b2 = 0
    self.b3 = 0
    self.set_up_stages_defs()
    self.values = [self.registry, self.channel_registry, self.module_type, self.stage_defs]
    self.var = tuple(self.values)
    self.baseline = self.values

  def setUp(self):
    # self.fs_id = set_ids['glg']
    # self.module_type = SuperSet.PROC
    # self.fset = module_creator_services.get(f'{self.module_type}-{self.fs_id}')
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_alt_props()
    self.set_up_var()
    self.comp = self.comp_class(*self.values,label=self.label)

# id: GLG
#     type_data:
#     name: Gateway Layer Groups
#     type: GATEWAY
#     purpose: serves as a global I/O center, & local plus global context matrix (and global map center as STN?)
#     cardinal_direction: dsc

# stages_to_groups_dict:
#   - id: noise_ctrl
#     groups: [noise_dwn_inhib,noise_adj_inhib]
#     total_count: 2
#   - id: cycle_relay
#     groups: [cycle_gate_ctrl,cycle_stg_adv]
#     total_count: 2
#   - id: cntxt_relay
#     groups: [cntxt_stg_adv,cntxt_up_inhib]
#     total_count: 2
#   - id: relay
#     groups: [relay_stg_adv]
#     total_count: 1

# this should be used to define the groups that get build
# group_details:
#   - id: noise_dwn_inhib
#     group_type: ORGANO
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: noise_adj_inhib
#     group_type: ORGANO
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cycle_gate_ctrl
#     group_type: ORGANO
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cycle_stg_adv
#     group_type: ORGANO
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cntxt_stg_adv
#     group_type: ORGANO
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cntxt_up_inhib
#     group_type: ORGANO
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: relay_stg_adv
#     group_type: ORGANO
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1

# relational_outputs:
#   noise_dwn_inhib: [self-cntxt_up_inhib;INHIBITOR;OVERLAY,cycle_relay;INHIBITOR;OVERLAY,cntxt_relay;INHIBITOR;OVERLAY]
#   noise_adj_inhib: [self-noise_dwn_inhib;INHIBITOR;OVERLAY]
#   cycle_gate_ctrl: [self-cycle_relay;INHIBITOR;OVERLAY]
#   cycle_stg_adv: [self-cycle_relay;ENERGIZER;OVERLAY,cntxt_ctrl;ENERGIZER;OVERLAY,proc_ctrl;ENERGIZER;OVERLAY]
#   cntxt_stg_adv: [self-cntxt_relay;ENERGIZER;OVERLAY,cntxt_ctrl;ENERGIZER;OVERLAY,proc_ctrl;ENERGIZER;OVERLAY]
#   cntxt_up_inhib: [self-cntxt_relay;INHIBITOR;OVERLAY]
#   relay_stg_adv: null


if __name__ == '__main__':
  unittest.main()
