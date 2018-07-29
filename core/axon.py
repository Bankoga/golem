# contains the definitions for cell axons
from usageLimits import *

class Axon():
    def __init__(self, origin, activation_type, terminal_destinations, chemical_type):
        """
        an axon needs to know the activation type which determines if the axon outputs a positive, negative, or chemical value
        'inhibitory' || 'excitory' || 'modulatory'
        it also needs to know where the axon terminates
        -1,1, or chemical is determined by activation type in conjunction with chemical type
        """
        self.value = self.get_value(activation_type, chemical_type)
        """ refresh rate, and activation rate can be implemented via usage limits but raises num ops per cell
        self.refreshRate
        self.activationRate
        """
        self.use_limits = UsageLimits()
        """
            destinations are determined by the cell location
            should we pass destinations to the axon from the cell instead of passing the cell location to the axon?
                That makes more sense I guess
        """
        self.destinations = terminal_destinations
        TODO: at present axons need to return their origin to enable consistent axon source ordering for the dendrites
        self.origin = origin

    def get_value(activation_type, chemical_type):
        if activation_type == 'inhibitory':
            return -1
        elif activation_type == 'excitory':
            return 1
        elif activation_type == 'modulatory' AND chemical_type != NULL:
            TODO: implement modulatory axon terminals
            raise SystemError('modulatory chemical type axons are not currently implemented')
        else:
            raise ValueError('either the activation_type was incorrect, or no chemical_type was supplied')

    def strength(self):
        TODO: implement so that that axon only checks during init which type of strength method to return based on value
        TODO: implement axons getting weaker as the capacity diminishes though this requires the axon be touched every timestep...
        return { self.destinations, self.origin, self.value }
    
    def reset(self):
        self.use_limits.reset()