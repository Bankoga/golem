---
type_data:
  id: DCLEG
  name: Decision Controlled Logos Encapsulator Group
  purpose: Represents one arbitrary cortical like shape that is affected by DM system outputs
  type: cortical
stages_to_groups_dict:
  - stage: cntxt_ctrl
    groups: [cntxt_dwn_inhib]
    total_count: 20
  - stage: init_proc
    groups: [ip_biinhib_ctrl,ip_down_inhib,ip_stg_adv]
    total_count: 20
  - stage: addt_proc
    groups: [ap_biinhib_ctrl,ap_down_inhib,ap_stg_adv]
    total_count: 20
  - stage: proc_ctrl
    groups: [c_biinhib_ctrl,c_down_inhib,c_up_inhib,c_stg_adv]
    total_count: 20
  - stage: out_proc
    groups: [op_biinhib_ctrl,op_down_inhib,op_stg_adv]
    total_count: 20
  - stage: cntxt_proc
    groups: [co_biinhib_ctrl,co_up_inhib,co_stg_adv]
    total_count: 20
group_details:
  - id: cntxt_dwn_inhib
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: ip_biinhib_ctrl
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: ip_down_inhib
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: ip_stg_adv
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: ap_biinhib_ctrl
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: ap_down_inhib
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: ap_stg_adv
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: c_biinhib_ctrl
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: c_down_inhib
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: c_up_inhib
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: c_stg_adv
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: op_biinhib_ctrl
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: op_down_inhib
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: op_stg_adv
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: co_biinhib_ctrl
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: co_up_inhib
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
  - id: co_stg_adv
    node_details:
      - node_type: Plate
        pct_of_group: 0
    pct_of_stage: 1
hooks:
  cntxt_from: [cntxt_dwn_inhib]
  cycle_from: [c_biinhib_ctrl,c_down_inhib,c_up_inhib,c_stg_adv]
hooks_outof:
  cntxt_to: [co_stg_adv]
  noise_to: [op_stg_adv,co_stg_adv]
  cycle_to: [op_stg_adv]
inputs:
  cntxt_dwn_inhib: null
  ip_biinhib_ctrl: null
  ip_down_inhib: null
  ip_stg_adv: null
  ap_biinhib_ctrl: null
  ap_down_inhib: null
  ap_stg_adv: null
  c_biinhib_ctrl: null
  c_down_inhib: null
  c_up_inhib: null
  c_stg_adv: null
  op_biinhib_ctrl: null
  op_down_inhib: null
  op_stg_adv: null
  co_biinhib_ctrl: null
  co_up_inhib: null
  co_stg_adv: null
outputs:
  cntxt_dwn_inhib: null
  ip_biinhib_ctrl: null
  ip_down_inhib: null
  ip_stg_adv: null
  ap_biinhib_ctrl: null
  ap_down_inhib: null
  ap_stg_adv: null
  c_biinhib_ctrl: null
  c_down_inhib: null
  c_up_inhib: null
  c_stg_adv: null
  op_biinhib_ctrl: null
  op_down_inhib: null
  op_stg_adv: null
  co_biinhib_ctrl: null
  co_up_inhib: null
  co_stg_adv: null
links_defined: null
links_used:
  - id: loop_i
...