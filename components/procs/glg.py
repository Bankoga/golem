from components.procs.proc import Proc
from data.axioms.configs import proc_ids

class GLG(Proc):
  def __init__(self):
    super.__init__(proc_ids['glg'])

class GLGBuilder():
  def __init__(self):
    pass
#     self._instance = None

  def __call__(self,**_ignored):
      return GLG()
#     if not self._instance:
#       self._instance = GLG()
#     return self._instance


# ---
# type_data:
#   id: GLG
#   name: Gateway Layer Groups
#   type: gateway
# stage_to_groups_dict:
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
# group_details:
#   - id: noise_dwn_inhib
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: noise_adj_inhib
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cycle_gate_ctrl
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cycle_stg_adv
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cntxt_stg_adv
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: cntxt_up_inhib
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
#   - id: relay_stg_adv
#     node_details:
#       - node_type: plate
#         pct_of_group: 1
#     pct_of_stage: -1
# inputs:
#   noise_dwn_inhib: [noise_adj_inhib-inhibitor,noise_ctrl-energy]
#   noise_adj_inhib: [noise_ctrl-energy]
#   cycle_gate_ctrl: [cycle_relay-energy,noise_dwn_inhib-inhibitor]
#   cycle_stg_adv: [cycle_relay-energy]
#   cntxt_stg_adv: [cntxt_relay-energy]
#   cntxt_up_inhib: [cntxt_relay-energy]
#   relay_stg_adv: null
# outputs:
#   noise_dwn_inhib: [cntxt_up_inhib-Inhbitor,cycle_relay-inhibitor,cntxt_relay-inhibitor]
#   noise_adj_inhib: [noise_dwn_inhib-inhibitor]
#   cycle_gate_ctrl: [cycle_relay-inhibitor]
#   cycle_stg_adv: [cycle_relay-energy,cntxt_ctrl-energy,proc_ctrl-energy]
#   cntxt_stg_adv: [cntxt_relay-energy,cntxt_ctrl-energy,proc_ctrl-energy]
#   cntxt_up_inhib: [cntxt_relay-inhibitor]
#   relay_stg_adv: null
# hooks_into:
#   noise_from: [noise_dwn_inhib,noise_adj_inhib]
#   cycle_from: [cycle_gate_ctrl,cycle_stg_adv]
#   cntxt_from: [cntxt_stg_adv,cntxt_up_inhib]
#   relay_from: [relay_stg_adv]
# hooks_outof:
#     cycle_to: [cycle_stg_adv]
#     cntxt_to: [cntxt_stg_adv]
#     relay_to: [relay_stg_adv]
# links_defined:
#   - id: loop_i
#     hooks_required:
#       - cntxt_from
#       - cntxt_to
#       - cycle_from
#       - cycle_to
#       - noise_from
#       - noise_to
#   - id: gate_i
#     hooks_required:
#       - relay_from
#       - relay_to
# links_used: null
# ...