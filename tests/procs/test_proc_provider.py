import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.configs import procs
from procs.proc import Proc
from procs.proc_provider import proc_services
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
  #   proc = read(module['type_data']['proc'],'proc')
  #   build_module_entry(module,module_num)
  #   self.assertTrue(module['proc_type_data']['id']=='GLG')
  #   # once we have the proc type config data, it must by converted into unified proc groups
  #   self.assertTrue(len(module['proc_groups'])==7)#17)
  #   # once we have the proc type config

  def test_set_inputs(self):
    for i,group_key in enumerate(module['proc_groups']):
      # we must check that the inputs have been added
      if module['inputs'] is not None:
         self.assertTrue(all(elem in module['inputs'] for elem in module['inputs']))
      for i,inp_key in enumerate(self.proc.inputs):
        if self.proc.inputs[inp_key] is not None:
          self.assertTrue(all(elem in module['inputs'] for elem in self.proc.inputs[inp_key]))
  
  def test_set_outputs(self):
    for i,group_key in enumerate(module['proc_groups']):
      # we must check that the outputs have been added
      if module['outputs'] is not None:
        self.assertTrue(all(elem in module['outputs'] for elem in module['outputs']))
      for i,out_key in enumerate(self.proc.outputs):
        if self.proc.outputs[out_key] is not None:
          self.assertTrue(all(elem in module['outputs'] for elem in self.proc.outputs[out_key]))
  
  def test_set_hooks_from(self):
    if ('hooks_outof' in proc):
      self.assertTrue(module['hooks_outof']==self.proc.hooks_outof)
    else:
      self.assertTrue(module['hooks_outof'] is None)
  
  def test_set_hooks_to(self):
    # we must check that the hooks have been added
    if ('hooks_into' in proc):
      self.assertTrue(module['hooks_into']==self.proc.hooks_into)
    else:
      self.assertTrue(module['hooks_into'] is None)
  
  def test_set_links_defined(self):
    # we must check that the links defined have been added
    if (self.proc.links_defined is None):
      self.assertTrue(module['links_defined'] is None)
    else:
      self.assertTrue(module['links_defined']== self.proc.links_defined)
    # we must check that the links used have been added
  
  def test_set_links_used(self):
    if (self.proc.links_used is None):
      self.assertTrue(module['links_used'] is None)
    else:
      self.assertTrue(module['links_used'] == self.proc.links_used)
  
  def test_set_stage_groups(self):
    for i,stage in enumerate(module['stages']):
      self.assertTrue(stage == (self.proc.stage_to_groups_dict[i]))
    # we must check that each group is created, and populated with the correct details

if __name__ == '__main__':
    unittest.main()