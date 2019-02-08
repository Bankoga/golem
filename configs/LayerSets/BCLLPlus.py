def BCLLPlus(input_shapes, assoc_shape, context_shape, meta_shapes):
    cellTypes = {
        'crown': {
            'read': function(inputSources,outputDestinations, outputFields), # this determines the primary shape of the input
            'outputFields': ['internal'],
            'readSource': ['L1'], # this will vary based on the layer it's used in
            'outputDestinatons': ['L2','L3'] # this will vary based on the layer it's used in
        },
        '': {
            'read': function,
            'outputFields': ['internal'],
        },
        '': {
            'read': function,
            'outputFields': ['internal'],
        },
        '': {
            'read': function,
            'outputFields': ['internal'],
        },
        '':  {
            'read': function,
            'outputFields': ['internal'],
        }
    }
    cellTypes['crown'].read('L1', ['L2','L3'], 'internal')

    How do we model the effects of cells on other cells inside this function?
    How do we model the effects 
    each separate output field has a unique function per input Shp types
    res_a = f(Layers Rules,inps=* in Input||Assoc||Context||Misc where Resource_T = A)
        return LayersRules(inps)
    res_b = f(Layers Rules,inps* in Input||Assoc||Context||Misc where Resource_T = B)
        return LayersRules(inps)
    LayersRules=f(input Shps, assoc Shp, context Shp, misc Shps, resourceT)
    n	L1	Contextual Inhib	Input, Alternate	Circuits	I->L2&L3 | A->L1'
    n	L2	Work, Initial	Input, Primary	Circuits, Melds, Pipelines	A->L3 | I->L5
    n	L3	Work, Follow Up	Input, Backup	Circuits, Melds, Pipelines	A->L5&6 | I->L6
    n	L5	Output, Direct	Output, Direct	Circuits, Module	A->[Direct Outputs]
    n	L6	Output, Indirect (Gateways)	Output, Alternate	Circuits, Module	A->[Indirect Outputs] | I->L2

    TAShps
    L1TAWhtShp = ?
    L2TAWhtShp = ?
    L3TAWhtShp = ?
    L5TAWhtShp = ?
    L6TAWhtShp = ?

    TBShps
    L1TBWhtShp = ?
    L2TBWhtShp = ?
    L3TBWhtShp = ?
    L5TBWhtShp = ?
    L6TBWhtShp = ?

    switch (resourceT)
        case A
        default
            L1 = TShps*L1TAWhtShp
            L2[TAShp] = TShps*L2TAWhtShp
            L3[TAShp] = TShps*L3TAWhtShp
            L5[TAShp] = TShps*L5TAWhtShp
            L6[TAShp] = TShps*L6TAWhtShp
        case B
            L1[TBShp] = TShps*L1TBWhtShp
            L2[TBShp] = TShps*L2TBWhtShp
            L3[TBShp] = TShps*L3TBWhtShp
            L5[TBShp] = TShps*L5TBWhtShp
            L6[TBShp] = TShps*L6TBWhtShp
        case C
            L1[TCShp] = TShps*L1TAWhtShp*0.4+TShps*L1TBWhtShp*0.6
            L2[TCShp] = TShps*L2TAWhtShp*0.4+TShps*L2TBWhtShp*0.6
            L3[TCShp] = TShps*L3TAWhtShp*0.4+TShps*L3TBWhtShp*0.6
            L5[TCShp] = TShps*L5TAWhtShp*0.4+TShps*L5TBWhtShp*0.6
            L6[TCShp] = TShps*L6TAWhtShp*0.4+TShps*L6TBWhtShp*0.6
    return L1 + L2 + L3 + L4 + L5 + L6
plasticityRules=f(resourceT, past_n_input_sets_of_type)
    switch(resourceT)
        case A
        default
            L1TAWhtShp = ?
            L2TAWhtShp = ?
            L3TAWhtShp = ?
            L5TAWhtShp = ?
            L6TAWhtShp = ?
        case B
            L1TBWhtShp = ?
            L2TBWhtShp = ?
            L3TBWhtShp = ?
            L5TBWhtShp = ?
            L6TBWhtShp = ?
        case C
            L1TAWhtShp = ?
            L1TBWhtShp = ?
            L2TAWhtShp = ?
            L2TBWhtShp = ?
            L3TAWhtShp = ?
            L3TBWhtShp = ?
            L5TAWhtShp = ?
            L5TBWhtShp = ?
            L6TAWhtShp = ?
            L6TBWhtShp = ?