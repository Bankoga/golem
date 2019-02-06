At every time step of golem operation, we have an active dictionary of all dest key:input shapes from the previous timestep which can be sent to any module that requests the appropriate dest key. These are used to generate the new list of all input shapes for the next time step
Each module has a unique set of input shapes that has to be generated. This set is defined by the module, and must correspond to the number of output shapes actually generated or else an error will be thrown
During init, we can read the config for each module, and build the dictionary of input shapes it requires

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
    'SynchIds': {
        'max_shape': MAX(1/2 shape dimension, 1)
    }
}