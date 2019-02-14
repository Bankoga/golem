from utils.linkers.linker import Linker

class GateILinker(Linker):
  def __init__(self):
    super().__init__('gate_i')
  
  def build_links(self):
    pass
    
class GateILinkerBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = GateILinker()
    return self._instance
