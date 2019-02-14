from linkers.linker import Linker

class SynchAllLinker(Linker):
  def __init__(self):
    super().__init__('synch_all')
  
  def build_links(self):
    pass
class SynchAllLinkerBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = SynchAllLinker()
    return self._instance