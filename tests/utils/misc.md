[G_i],Energy
[G_i-CycleRelay],Energy
[G_i-NoiseCtrl],Energy
[G_i-CntxtRelay],Energy
[Gate_i],Energy
NoiseCtrl:NoiseDwnInhib,NoiseAdjInhib
CycleRelay:CycleGateCtrl,CycleStgAdv
CntxtRelay:CntxtStgAdv,CntxtUpInhib
Relay:StgAdv

G_i-NoiseCtrl:G_i
G_i-CycleRelay:G_i
G_i-CntxtRelay:G_i
Gate_i-Relay:Gate_i

*: [G_i,Energy]
NoiseDwnInhib: [G_i-NoiseDwnInhibPrev,Bool,NoiseAdjInhib,Energy,G_i-NoiseCtrl,Energy]
NoiseAdjInhib: [G_i-NoiseAdjInhibPrev,Bool,G_i-NoiseCtrl,Energy]
CycleGateCtrl: [G_i-CycleStgAdvPrev,Bool,G_i-CycleRelay,Energy]
CycleStgAdv: [G_i-CycleStgAdvPrev,Bool,G_i-CycleRelay,Energy]
CntxtStgAdv: [G_i-CntxtStgAdvPrev,Bool,G_i-CntxtRelay,Energy]
CntxtUpInhib: [G_i-CntxtUpInhibPrev,Bool,G_i-CntxtRelay,Energy]
Relay: [Gate_i,Energy, Gate_i-Prev,Bool]

NoiseDwnInhib: [Plate,1],1
NoiseAdjInhib: [Plate,1],1
CycleGateCtrl: [Point,1],1
CycleStgAdv: [Point,1],1
CntxtStgAdv: [Plate,1],1
CntxtUpInhib: [Plate,1],1
Relay:[Point,1],1

NoiseDwnInhib: [G_i-CntxtUpInhib,Inhbitor,G-CycleRelay,Inhibitor,G-CntxtRelay,Inhibitor]
NoiseAdjInhib: [G_i-NoiseDwnInhib,Inhibitor]
CycleGateCtrl: [G_i-CycleRelay,Inhibitor]
CycleStgAdv: [G_i-CycleRelay,Energy,G_i-CntxtCtrl,Energy,G_i-ProcCtrl,Energy]
CntxtStgAdv: [G_i-CntxtRelay,Energy,G_i-CntxtCtrl,Energy,G_i-ProcCtrl,Energy]
CntxtUpInhib: [G_i-CntxtRelay,Inhibitor]
Relay:[Gate_i-]

G_i-ProcCtrl,Energy
G_i-CntxtCtrl,Energy
G_i-NoiseCtrl,Energy
OutputCtrl-G_i,Energy

If every link has subdest keys, then we can define them separately from the InputMelds,&ProcGroupInputMelds
ProcGroups produce ouput however. If links only use the processed versions of the module output, we can ignore defining proc group to proc group specific mappings
ShapeComposition is the key here
G_i
G_i,Energy
G_i-CycleRelay
G_i-CycleRelay,Energy
G_i-NoiseCtrl
G_i-NoiseCtrl,Energy
G_i-CntxtRelay
G_i-CntxtRelay,Energy
G_i-NoiseDwnInhibPrev,Bool
G_i-NoiseAdjInhib,Energy
G_i-NoiseAdjInhibPrev,Bool
G_i-CycleStgAdvPrev,Bool
G_i-CntxtStgAdvPrev,Bool
G_i-CntxtUpInhibPrev,Bool
G_i-CntxtUpInhib,Inhbitor
G-CycleRelay,Inhibitor
G-CntxtRelay,Inhibitor
G_i-NoiseDwnInhib,Inhibitor
G_i-CycleRelay,Inhibitor
G_i-CntxtRelay,Inhibitor
G_i-ProcCtrl,Energy
G_i-CntxtCtrl,Energy
B1,Energy
TestInput,Energy,TestInputWhl
G_TestA-ProcCtrl,Energy,TestInputWhl
G_TestA-CntxtCtrl,Energy,TestInputWhl