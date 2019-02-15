import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.configs import procs
from components.procs.proc import Proc
from components.procs.proc_provider import proc_services
import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
from utils.config_reader import read
from utils.config_operations import build_full_config
from utils.config_operations import build_module_entry
from data.axioms.pos_maps import package_map, pipeline_map
from data.axioms.configs import proc_ids, file_type
from utils.config_reader import read

def _check_results_contains_property_from_parts_(self, result, prop, part):
  if (part[prop] is None):
    self.assertTrue(result[prop] is None)
  else:
    self.assertTrue(result[prop].contains(part[prop]))

class TestProcProvider(unittest.TestCase):
  def setUp(self):
    self.proc_id = proc_ids['glg']
    self.proc =  proc_services.get(self.proc_id, **{})
    self.proc_conf = read(self.proc_id,file_type['proc'])

  # @given(st.sampled_from(procs))
  # def test_get(self, proc_id):
  #   proc = proc_services.get(proc_id, **{})
  #   self.assertTrue(proc.get_id(), proc_id)
    
  # # @given(st.integers(max_value=6))
  # def test_build_module_entry(self):
  #   module_num = 7
  #   module = self.config['modules'][module_num]
  #   # building a module config means turning all of the properties into a single list of processing group properties ready for melding
  #   # thus building a module config is composed of several steps. In essence, we extend the module object using the proc object
  #   # first we must collect the missing proc type information from the corresponding config
  #   proc = read(self.proc['type_data']['proc'],'proc')
  #   build_module_entry(module,module_num)
  #   self.assertTrue(self.proc['proc_type_data']['id']=='GLG')
  #   # once we have the proc type config data, it must by converted into unified proc groups
  #   self.assertTrue(len(self.proc['proc_groups'])==7)#17)
  #   # once we have the proc type config

  WHAT ARE THE PROPERTIES OF A PROC OBJECT THAT REFLECT THE SUCCESS OF THE METHOD BEING TESTED!

  def test_set_inputs(self):
    for i,group_key in enumerate(self.proc['proc_groups']):
      # we must check that the inputs have been added
      if self.proc['inputs'] is not None:
         self.assertTrue(all(elem in self.proc['inputs'] for elem in self.proc['inputs']))
      for i,inp_key in enumerate(self.proc_conf['inputs']):
        if self.proc_conf['inputs'][inp_key] is not None:
          self.assertTrue(all(elem in self.proc['inputs'] for elem in self.proc_conf['inputs'][inp_key]))
  
  def test_set_outputs(self):
    for i,group_key in enumerate(self.proc['proc_groups']):
      # we must check that the outputs have been added
      if self.proc['outputs'] is not None:
        self.assertTrue(all(elem in self.proc['outputs'] for elem in self.proc['outputs']))
      for i,out_key in enumerate(self.proc_conf['outputs']):
        if self.proc_conf['outputs'][out_key] is not None:
          self.assertTrue(all(elem in self.proc['outputs'] for elem in self.proc_conf['outputs'][out_key]))
  
  def test_set_hooks_from(self):
    if ('hooks_outof' in self.proc_conf):
      self.assertTrue(self.proc['hooks_outof']==self.proc_conf['hooks_outof'])
    else:
      self.assertTrue(self.proc['hooks_outof'] is None)
  
  def test_set_hooks_to(self):
    # we must check that the hooks have been added
    if ('hooks_into' in self.proc_conf):
      self.assertTrue(self.proc['hooks_into']==self.proc_conf['hooks_into'])
    else:
      self.assertTrue(self.proc['hooks_into'] is None)
  
  def test_set_links_defined(self):
    # we must check that the links defined have been added
    if (self.proc_conf['links_defined'] is None):
      self.assertTrue(self.proc['links_defined'] is None)
    else:
      self.assertTrue(self.proc['links_defined']== self.proc_conf['links_defined'])
    # we must check that the links used have been added
  
  def test_set_links_used(self):
    if (self.proc_conf['links_used'] is None):
      self.assertTrue(self.proc['links_used'] is None)
    else:
      self.assertTrue(self.proc['links_used'] == self.proc_conf['links_used'])
  
  def test_set_stage_groups(self):
    for i,stage in enumerate(self.proc['stages']):
      self.assertTrue(stage == (self.proc_conf['stage_to_groups_dict'][i]))
    # we must check that each group is created, and populated with the correct details

if __name__ == '__main__':
    unittest.main()