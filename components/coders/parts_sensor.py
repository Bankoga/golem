from components.coders.coder import Coder
from data.axioms.configs import coder_ids

class PartsSensor(Coder):
  def __init__(self):
    super().__init__(coder_ids['ps'])

class PartsSensorBuilder():
  def __init__(self):
    pass
  def __call__(self,**_ignored):
      return PartsSensor()