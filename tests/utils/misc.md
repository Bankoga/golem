[G_i],Energy
[G_i-cycle_relay],Energy
[G_i-noise_ctrl],Energy
[G_i-cntxt_relay],Energy
[Gate_i],Energy
noise_ctrl:noise_dwn_inhib,noise_adj_inhib
cycle_relay:cycle_gate_ctrl,cycle_stg_adv
cntxt_relay:cntxt_stg_adv,cntxt_up_inhib
relay:stg_adv

G_i-noise_ctrl:G_i
G_i-cycle_relay:G_i
G_i-cntxt_relay:G_i
Gate_i-relay:Gate_i

*: [G_i,Energy]
noise_dwn_inhib: [G_i-noise_dwn_inhibPrev,Bool,noise_adj_inhib,Energy,G_i-noise_ctrl,Energy]
noise_adj_inhib: [G_i-noise_adj_inhibPrev,Bool,G_i-noise_ctrl,Energy]
cycle_gate_ctrl: [G_i-cycle_stg_advPrev,Bool,G_i-cycle_relay,Energy]
cycle_stg_adv: [G_i-cycle_stg_advPrev,Bool,G_i-cycle_relay,Energy]
cntxt_stg_adv: [G_i-cntxt_stg_advPrev,Bool,G_i-cntxt_relay,Energy]
cntxt_up_inhib: [G_i-cntxt_up_inhibPrev,Bool,G_i-cntxt_relay,Energy]
relay: [Gate_i,Energy, Gate_i-Prev,Bool]

noise_dwn_inhib: [Plate,1],1
noise_adj_inhib: [Plate,1],1
cycle_gate_ctrl: [Point,1],1
cycle_stg_adv: [Point,1],1
cntxt_stg_adv: [Plate,1],1
cntxt_up_inhib: [Plate,1],1
relay:[Point,1],1

noise_dwn_inhib: [G_i-cntxt_up_inhib,Inhbitor,G-cycle_relay,Inhibitor,G-cntxt_relay,Inhibitor]
noise_adj_inhib: [G_i-noise_dwn_inhib,Inhibitor]
cycle_gate_ctrl: [G_i-cycle_relay,Inhibitor]
cycle_stg_adv: [G_i-cycle_relay,Energy,G_i-cntxt_ctrl,Energy,G_i-proc_ctrl,Energy]
cntxt_stg_adv: [G_i-cntxt_relay,Energy,G_i-cntxt_ctrl,Energy,G_i-proc_ctrl,Energy]
cntxt_up_inhib: [G_i-cntxt_relay,Inhibitor]
relay:[Gate_i-]

G_i-proc_ctrl,Energy
G_i-cntxt_ctrl,Energy
G_i-noise_ctrl,Energy
OutputCtrl-G_i,Energy

If every link has subdest keys, then we can define them separately from the InputMelds,&ProcGroupInputMelds
ProcGroups produce ouput however. If links only use the processed versions of the module output, we can ignore defining proc group to proc group specific mappings
ShapeComposition is the key here
G_i
G_i,Energy
G_i-cycle_relay
G_i-cycle_relay,Energy
G_i-noise_ctrl
G_i-noise_ctrl,Energy
G_i-cntxt_relay
G_i-cntxt_relay,Energy
G_i-noise_dwn_inhibPrev,Bool
G_i-noise_adj_inhib,Energy
G_i-noise_adj_inhibPrev,Bool
G_i-cycle_stg_advPrev,Bool
G_i-cntxt_stg_advPrev,Bool
G_i-cntxt_up_inhibPrev,Bool
G_i-cntxt_up_inhib,Inhbitor
G-cycle_relay,Inhibitor
G-cntxt_relay,Inhibitor
G_i-noise_dwn_inhib,Inhibitor
G_i-cycle_relay,Inhibitor
G_i-cntxt_relay,Inhibitor
G_i-proc_ctrl,Energy
G_i-cntxt_ctrl,Energy
B1,Energy
TestInput,Energy,TestInputWhl
G_TestA-proc_ctrl,Energy,TestInputWhl
G_TestA-cntxt_ctrl,Energy,TestInputWhl