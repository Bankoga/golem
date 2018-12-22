class Encoder:
    """
    A special type of problem domain that cannot be handled by the problem domain class.
    Each encoder parses external input for internal consumption, and thus each one requires different code for translating to spikes.
    """
    def __init__(self, type, outputs):
        """
        create a new encoder object of the corresponding sensor type
        """