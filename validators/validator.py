import utils.object_factory

class Validator:
  """
    This is the base factory class that is called to validate any part of a config
    I opened this, not because of all the factory stuff I added to it. Though it was intended for that eventually
    I opened this for adding a note to treat writing this as answering the question of
    What are the properties of each type of config item
    Things like, are all ids kept in a type data object, or can they be stored wihout said object
    Are null inputs and outputs lists valid? When are the valid? When are they invalid?

    Different types of things that require validation
    - Full Golem Type Config
    - Module Full Entry
    - Link usage
    - Link composition
  """
# Omitting other implementation classes shown above
  def __init__(self, validator_id):
    self.id = validator_id