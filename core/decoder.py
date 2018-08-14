class Decoder:
    """
    A special type of problem domain that cannot be handled by the problem domain class.
    Each decoder parses internal input for external consumption, and thus each one requires different code for translating from spikes.
    """
    def __init__(self, type, outputs):
        TODO: create the type of decoder