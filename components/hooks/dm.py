from components.hooks.linker import Linker

class DmLinker(Linker):
  def __init__(self):
    super().__init__('dm')
  
  def build_links(self):
    pass

class DmLinkerBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,**_ignored):
    if not self._instance:
      self._instance = DmLinker()
    return self._instance
