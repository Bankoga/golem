from components.enums.prop_types import GroupType, RsrcType
from components.axioms.cell_types import CellType

stage_defs = [
  {
    'label': 'noise_ctrl',
    'groups': ['noise_dwn_inhib','noise_adj_inhib']
  },
  {
    'label': 'cycle_relay',
    'groups': ['cycle_gate_ctrl','cycle_stg_adv']
  },
  {
    'label': 'cntxt_relay',
    'groups': ['cntxt_stg_adv','cntxt_up_inhib']
  },
  {
    'label': 'relay',
    'groups': ['relay_stg_adv']
  },
]

group_defs = [
  {
    'label': 'noise_dwn_inhib',
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
    'label': 'noise_adj_inhib',
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
    'label': 'cycle_gate_ctrl',
    'group_type': GroupType.ORGANO,
    'node_details':[
      {
        'node_type': CellType.PLATE,
        'pct_of_group': 1
      }],
    'pct_of_stage': -1
  },
  {
    'label': 'cycle_stg_adv',
    'group_type': GroupType.ORGANO,
    'node_details':[
      {
        'node_type': CellType.PLATE,
        'pct_of_group': 1
      }],
    'pct_of_stage': -1
  },
  {
    'label': 'cntxt_stg_adv',
    'group_type': GroupType.ORGANO,
    'node_details':[
      {
        'node_type': CellType.PLATE,
        'pct_of_group': 1
      }],
    'pct_of_stage': -1
  },
  {
    'label': 'cntxt_up_inhib',
    'group_type': GroupType.ORGANO,
    'node_details':[
      {
        'node_type': CellType.PLATE,
        'pct_of_group': 1
      }],
    'pct_of_stage': -1
  },
  {
    'label': 'relay_stg_adv',
    'group_type': GroupType.ORGANO,
    'node_details':[
      {
        'node_type': CellType.PLATE,
        'pct_of_group': 1
      }],
    'pct_of_stage': -1
  }
]