# contains definition for the chemicalState of a layer or cell
# chemicalState affects/modulates the functions of cells

class ChemicalState():
    ap_thresh_mod = 0
    synapse_weight_mod = 0
    dendrite_sensitivity_mod = 0
    axon_strength_mod = 0

    def consumeChemical(chem_type, chem_quantity):
        # update the appropriate properties based on the chemName, and amount of chemicals

    def resetState():
        ap_thresh_mod, synapse_weight_mod, dendrite_sensitivity_mod, axon_strength_mod = 0
