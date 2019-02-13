import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
from utils.config_reader import read
from utils.config_operations import build_full_config
from utils.config_operations import build_module_entry

def _check_results_contains_property_from_parts_(self, result, prop, part):
  if (part[prop] is None):
    self.assertTrue(result[prop] is None)
  else:
    self.assertTrue(result[prop].contains(part[prop]))


class TestConfigOperations(unittest.TestCase):

  def setUp(self):
    self.config = read('Test','golem')

  def test_build_full_config(self):
    full = build_full_config(self.config)
    self.assertTrue(full['modules'][0]['proc_groups']['type_data']['id']=='PICG')
    self.assertNotEqual(self.config,full)

  # @given(st.integers(max_value=6))
  def test_build_module_entry(self):
    module_num = 2
    module = self.config['modules'][module_num]
    # building a module config means turning all of the properties into a single list of processing group properties ready for melding
    # thus building a module config is composed of several steps. In essence, we extend the module object using the proc object
    # first we must collect the missing proc type information from the corresponding config
    proc = read(module['type_data']['proc'],'proc')
    results = build_module_entry(module,module_num)
    self.assertTrue(results['proc_type_data']['id']=='DCLEG')
    # once we have the proc type config data, it must by converted into unified proc groups
    self.assertTrue(len(results['proc_groups'])==17)
    # once we have the proc type config
    for i,stage in enumerate(results['stages']):
      self.assertTrue(stage == (proc['stage_to_groups_dict'][i]))
    # we must check that each group is created, and populated with the correct details
    for i,group_key in enumerate(results['proc_groups']):

      # we must check that the group has the correct location,positions data
      self.assertEqual(results['proc_groups'][group_key]['pos_data']['x'],0)

      # we must check that the inputs have been added
      if module['inputs'] is not None:
        self.assertTrue(results['proc_groups'][group_key]['inputs'].contains(module['inputs']))
      for i,inp_key in enumerate(proc['inputs']):
        if proc['inputs'][inp_key] is not None:
          self.assertTrue(results['proc_groups'][group_key]['inputs'].contains(proc['inputs'][inp_key]))

      # we must check that the outputs have been added
      if module['outputs'] is not None:
        self.assertTrue(results['proc_groups'][group_key]['outputs'].contains(module['outputs']))
      for i,out_key in enumerate(proc['outputs']):
        if proc['outputs'][out_key] is not None:
          self.assertTrue(results['proc_groups'][group_key]['outputs'].contains(proc['outputs'][out_key]))

      # # we must check that the hooks have been added
      # if ('hooks_into' in proc and group_key in proc['hooks_into']):
      #   self.assertTrue(results['proc_groups'][group_key]['hooks_into'] is None)
      # else:
      #   self.assertTrue(results['proc_groups'][group_key]['hooks_into'].contains(proc['hooks_into'][group_key]))
      # if ('hooks_outof' in proc and group_key in proc['hooks_outof']):
      #   self.assertTrue(results['proc_groups'][group_key]['hooks_outof'] is None)
      # else:
      #   self.assertTrue(results['proc_groups'][group_key]['hooks_outof']==proc['hooks_outof'][group_key])
      
    # we must check that the hooks have been added
    if ('hooks_into' in proc):
      self.assertTrue(results['hooks_into']==proc['hooks_into'])
    else:
      self.assertTrue(results['hooks_into'] is None)
    if ('hooks_outof' in proc):
      self.assertTrue(results['hooks_outof']==proc['hooks_outof'])
    else:
      self.assertTrue(results['hooks_outof'] is None)

    # we must check that the links defined have been added
    if (proc['links_defined'] is None):
      self.assertTrue(results['links_defined'] is None)
    else:
      self.assertTrue(results['links_defined']== proc['links_defined'])
    # we must check that the links used have been added
    if (proc['links_used'] is None):
      self.assertTrue(results['links_used'] is None)
    else:
      self.assertTrue(results['links_used'] == proc['links_used'])


if __name__ == '__main__':
    unittest.main()