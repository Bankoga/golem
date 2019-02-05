At every time step of golem operation, we have an active dictionary of all dest key:input shapes from the previous timestep which can be sent to any module that requests the appropriate dest key. These are used to generate the new list of all input shapes for the next time step
Each module has a unique set of input shapes that has to be generated. This set is defined by the module, and must correspond to the number of output shapes actually generated or else an error will be thrown
During init, we can read the config for each module, and build the dictionary of input shapes it requires

Internal Melds (wht bt fld mpngs?): BCCL+(InputA, [Destinations])
  InputA -> Repo, Characters
  InputA -> Repo, Tokens
  InputA -> Repo, Phrases
  InputA -> Repo, InputA
Output Melds: Energy->Concept Eval Ctrlr
Output Semantic Field Sizes:
16 of 1/16 Len in InputA-Ch, 4 Keys (all keys are for assoc or mapping but then they become a separate stream)
8 of 1/8 Len in InputA-Tk, 4 Keys
4 of 1/4 Len in InputA-Ph, 4 Keys
InputA, 4 Keys

In- & Out- Are added to fields within functions to denote afference vs efference.
Fields = {
    'AWhl': {
        'max_shape': 1 x 8*8+1*8+8*8+1*8 = 1 x 144
    },
    'AAtm': {
        'max_shape': 1 x 144/16 = 1 x 9
    },
    'ATkn': {
        'max_shape': 1 x 144/8 = 1 x 18
    },
    'APrt': {
        'max_shape': 1 x 144/4 = 1 x 36
    },
    '': {
        'max_shape': 1 x ?
    }
}
Extractor Circuit
Expected Input Fields
- InAWhl
Generated Output Fields broken into the number of field shapes used to generate them
- OutFunAtms: np.array_split(16, InAWhl)
- OutFunTkns: np.array_split(8, InAWhl)
- OutFunPrts: np.array_split(4, InAWhl)
- OutFunWhl: Join(InAAtms) + Join(InATkns) + Join(InAPrts) + InAWhl