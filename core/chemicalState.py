# contains definition for the chemicalState of a layer or cell
# chemicalState affects/modulates the functions of cells
from usageLimits import *

TODO: implement a chemical class that can be used to handles types, their effects, and different strengths of effect
class ChemicalState():
    def __init__():
        self.ap_thresh_mod = 0
        self.synapse_weight_mod = 0
        self.dendrite_sensitivity_mod = 0
        self.axon_strength_mod = 0
        self.use_limits_mods = UsageLimits()

    def consume_chemical(chem_type, chem_quantity):
        # update the appropriate properties based on the chemName, and amount of chemicals

    def reset_state(self):
        self.ap_thresh_mod, self.synapse_weight_mod, self.dendrite_sensitivity_mod, self.axon_strength_mod = 0
        self.use_limits_mod = UsageLimits()
