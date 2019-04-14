from components.enums.prop_types import GroupType, ResourceType, ChannelType,ModuleType
from components.axioms.cell_types import CellType


type_data = {
  'name': 'Gateway Layer Groups',
  'type': ModuleType.GATEWAY,
  'purpose': "serves as a global I/O center, & local plus global context matrix (and global map center as STN?)",
  'cardinal_direction': 'dsc'
}

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

relational_output_defs = {
  'noise_dwn_inhib': [
    {
      'recipient': 'self-cntxt_up_inhib',
      'resource_type': ResourceType.INHIBITOR,
      'channel_type': ChannelType.OVERLAY,
    },
    {
      'recipient': 'cycle_relay',
      'resource_type': ResourceType.INHIBITOR,
      'channel_type': ChannelType.OVERLAY,
    },
    {
      'recipient': 'cntxt_relay',
      'resource_type': ResourceType.INHIBITOR,
      'channel_type': ChannelType.OVERLAY,
    }
  ],
  'noise_adj_inhib': [
    {
      'recipient': 'self-noise_dwn_inhib',
      'resource_type': ResourceType.INHIBITOR,
      'channel_type': ChannelType.OVERLAY,
    }
  ],
  'cycle_gate_ctrl': [
    {
      'recipient': 'self-cycle_relay',
      'resource_type': ResourceType.INHIBITOR,
      'channel_type': ChannelType.OVERLAY,
    }
  ],
  'cycle_stg_adv': [
    {
      'recipient': 'self-cycle_relay',
      'resource_type': ResourceType.ENERGIZER,
      'channel_type': ChannelType.OVERLAY,
    },
    {
      'recipient': 'cntxt_ctrl',
      'resource_type': ResourceType.ENERGIZER,
      'channel_type': ChannelType.OVERLAY,
    },
    {
      'recipient': 'proc_ctrl',
      'resource_type': ResourceType.ENERGIZER,
      'channel_type': ChannelType.OVERLAY,
    }
  ],
  'cntxt_stg_adv': [
    {
      'recipient': 'self-cntxt_relay',
      'resource_type': ResourceType.ENERGIZER,
      'channel_type': ChannelType.OVERLAY,
    },
    {
      'recipient': 'cntxt_ctrl',
      'resource_type': ResourceType.ENERGIZER,
      'channel_type': ChannelType.OVERLAY,
    },
    {
      'recipient': 'proc_ctrl',
      'resource_type': ResourceType.ENERGIZER,
      'channel_type': ChannelType.OVERLAY,
    }
  ],
  'cntxt_up_inhib': [
    {
      'recipient': 'self-cntxt_relay',
      'resource_type': ResourceType.INHIBITOR,
      'channel_type': ChannelType.OVERLAY,
    }
  ],
  'relay_stg_adv': None
}