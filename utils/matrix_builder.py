from data.axioms.configs import file_type
from utils.config_reader import read

class Matrix:
  def __init__(self, proc_id):
    self.config = read(proc_id,file_type['proc'])
    self.id = self.config['type_data']['id']
    self.name = self.config['type_data']['name']
    self.type = self.config['type_data']['type']
    self.purpose = self.config['type_data']['purpose']
    self.groups = dict()
  
  def get_id(self):
    return self.id
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_inputs_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_outputs_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_hooks_from_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_hooks_to_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_links_defined_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_links_used_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_stage_groups_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_proc_groups_(self):
    pass
  
  @abstractmethod # pylint: disable=undefined-variable
  def _set_stages_(self):
    pass


class MatrixBuilder():
  def __init__(self):
    self._instance = None

  def __call__(self,proc_id,**_ignored):
    return Matrix(proc_id)
    # if not self._instance:
    #   self._instance = GLG()
    # return self._instance
