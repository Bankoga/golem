from linkers.linker import Linker

class LoopILinker(Linker):
  def __init__(self):
    super().__init__('loop_i')
  
  def build_links(self):
    pass

class LoopILinkerBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = LoopILinker()
    return self._instance
