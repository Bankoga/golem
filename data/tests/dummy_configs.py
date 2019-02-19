
module_all_groups = {
  "type_data": {
      'id': 'TestC',
      'proc': 'PICG'
    },
    'outputs': [],
    'shape_of_groups_dict': {
      'field_name': '*'
    },
    'channels': 1,
    'package': 'shell',
    'pipeline': 'input'
}
module_null_groups = {
  "type_data": {
      'id': 'TestB',
      'proc': 'PICG'
    },
    'outputs': [],
    'shape_of_groups_dict': {
      'field_name': '*'
    },
    'channels': 1,
    'package': 'shell',
    'pipeline': 'input'
}
module_specific_groups = {
  "type_data": {
      'id': 'TestA',
      'proc': 'PICG'
    },
    'outputs': [],
    'shape_of_groups_dict': {
      'field_name': ['cntxt_dwn_inhib','ip_biinhib_ctrl','ip_down_inhib','ip_stg_adv','ap_biinhib_ctrl','ap_down_inhib','ap_stg_adv','c_biinhib_ctrl','c_down_inhib','c_up_inhib','c_stg_adv','op_biinhib_ctrl','op_down_inhib','op_stg_adv','co_biinhib_ctrl','co_up_inhib','co_stg_adv']
    },
    'channels': 1,
    'package': 'shell',
    'pipeline': 'input'
}