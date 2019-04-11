import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.mediators.procs.proc_provider import proc_services
from components.axioms.configs import file_type, proc_ids
from tests.components.mediators.procs.test_proc import TestProc
from utils.config_reader import read

import unittest

from hypothesis import given, reproduce_failure
from hypothesis import strategies as st
from numpy import append, array

from components.axioms.configs import file_type, proc_ids, set_ids
from components.enums.prop_types import ChannelType, ModuleType
from components.mediators.procs.proc import Proc
from components.mediators.procs.proc_provider import proc_services
from tests.components.mediators.test_module import TestModule
from tests.strategies.module_strats import (group_input_set, module_input_set,
                                            unbuilt_module_input_set)
from utils.cardinators.cardinator_provider import cardinator_services
from utils.config_reader import read
from utils.misc import heapsort

class TestGLG(TestModule):

  # TODO: get GLG working the new way as if it was just read in by a config
  def setUp(self):
    self.proc_id = proc_ids['glg']
    self.proc =  proc_services.get(self.proc_id, **{})
    self.proc_conf = read(self.proc_id,file_type['proc'])
    id: GLG
    type_data:
    name: Gateway Layer Groups
    type: GATEWAY
    purpose: serves as a global I/O center, & local plus global context matrix (and global map center as STN?)
    cardinal_direction: dsc

stages_to_groups_dict:
  - id: noise_ctrl
    groups: [noise_dwn_inhib,noise_adj_inhib]
    total_count: 2
  - id: cycle_relay
    groups: [cycle_gate_ctrl,cycle_stg_adv]
    total_count: 2
  - id: cntxt_relay
    groups: [cntxt_stg_adv,cntxt_up_inhib]
    total_count: 2
  - id: relay
    groups: [relay_stg_adv]
    total_count: 1

this should be used to define the groups that get build
group_details:
  - id: noise_dwn_inhib
    group_type: ORGANO
    node_details:
      - node_type: plate
        pct_of_group: 1
    pct_of_stage: -1
  - id: noise_adj_inhib
    group_type: ORGANO
    node_details:
      - node_type: plate
        pct_of_group: 1
    pct_of_stage: -1
  - id: cycle_gate_ctrl
    group_type: ORGANO
    node_details:
      - node_type: plate
        pct_of_group: 1
    pct_of_stage: -1
  - id: cycle_stg_adv
    group_type: ORGANO
    node_details:
      - node_type: plate
        pct_of_group: 1
    pct_of_stage: -1
  - id: cntxt_stg_adv
    group_type: ORGANO
    node_details:
      - node_type: plate
        pct_of_group: 1
    pct_of_stage: -1
  - id: cntxt_up_inhib
    group_type: ORGANO
    node_details:
      - node_type: plate
        pct_of_group: 1
    pct_of_stage: -1
  - id: relay_stg_adv
    group_type: ORGANO
    node_details:
      - node_type: plate
        pct_of_group: 1
    pct_of_stage: -1

relational_outputs:
  noise_dwn_inhib: [self-cntxt_up_inhib;INHIBITOR;OVERLAY,cycle_relay;INHIBITOR;OVERLAY,cntxt_relay;INHIBITOR;OVERLAY]
  noise_adj_inhib: [self-noise_dwn_inhib;INHIBITOR;OVERLAY]
  cycle_gate_ctrl: [self-cycle_relay;INHIBITOR;OVERLAY]
  cycle_stg_adv: [self-cycle_relay;ENERGIZER;OVERLAY,cntxt_ctrl;ENERGIZER;OVERLAY,proc_ctrl;ENERGIZER;OVERLAY]
  cntxt_stg_adv: [self-cntxt_relay;ENERGIZER;OVERLAY,cntxt_ctrl;ENERGIZER;OVERLAY,proc_ctrl;ENERGIZER;OVERLAY]
  cntxt_up_inhib: [self-cntxt_relay;INHIBITOR;OVERLAY]
  relay_stg_adv: null


if __name__ == '__main__':
  unittest.main()
