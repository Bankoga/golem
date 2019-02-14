from utils.linkers.linker import Linker

class SynchILinker(Linker):
  def __init__(self):
    super().__init__('synch_i')
  
  def build_links(self):
    pass
class SynchILinkerBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = SynchILinker()
    return self._instance
