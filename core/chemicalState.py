# contains definition for the chemicalState of a layer or cell
# chemicalState affects/modulates the functions of cells
from usageLimits import *

class ChemicalState():
    def __init__():
        self.ap_thresh_mod = 0
        self.synapse_weight_mod = 0
        self.dendrite_sensitivity_mod = 0
        self.axon_strength_mod = 0
        self.use_limits_mods = UsageLimits()

    def consumeChemical(chem_type, chem_quantity):
        # update the appropriate properties based on the chemName, and amount of chemicals

    def resetState():
        self.ap_thresh_mod, self.synapse_weight_mod, self.dendrite_sensitivity_mod, self.axon_strength_mod = 0
        self.use_limits_mod = UsageLimits()
