from components.matrix.registry import Registry
from utils.validators.matrix import channel_item_check

class ChannelRegistry(Registry):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def add_item(self, new_item):
    if channel_item_check(new_item):
      self._dup_safe_add(new_item)
    else:
      raise RuntimeError('Cannot add invalid item to registry!')