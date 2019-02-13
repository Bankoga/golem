import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
from utils.config_reader import read
from utils.config_operations import build_full_config
from utils.config_operations import build_module_entry

class TestConfigOperations(unittest.TestCase):

  def setUp(self):
    self.config = read('Test','golem')

  def test_build_full_config(self):
    full = build_full_config(self.config)
    # self.assertTrue([]]['proc_groups']['type_data']['id']=='CCG'))
    self.assertNotEqual(self.config,full)

  def test_build_module_entry(self):
    module = self.config['modules'][0]
    # building a module config means turning all of the properties into a single list of processing group properties ready for melding
    # thus building a module config is composed of several steps. In essence, we extend the module object using the proc object
    # first we must collect the missing proc type information from the corresponding config
    proc = read(module['type_data']['proc'],'proc')
    results = build_module_entry(module,0)
    self.assertTrue(results['type_data']['id']=='PICG')
    # once we have the proc type config data, it must by converted into unified proc groups
    self.assertTrue(len(results['proc_groups'])==1)
    # once we have the proc type config
    for i,stage in enumerate(results['stages']):
      self.assertTrue(stage == (proc['stage_to_groups_dict'][i]))
    # we must check that each group is created, and populated with the correct details
    for i,group_key in enumerate(results['proc_groups']):
      # we must check that the group has the correct location,positions data
      self.assertEqual(results['proc_groups'][group_key]['pos_data']['x'],0)
      # we must check that the inputs have been added
      # self.assertTrue(results['proc_groups'][group_key]['inputs'].contains(module['inputs']))
      # self.assertTrue(results['proc_groups'][group_key]['inputs'].contains(proc['inputs']))
      # we must check that the outputs have been added
      # self.assertTrue(results['proc_groups'][group_key]['outputs'].contains(module['outputs']))
      # self.assertTrue(results['proc_groups'][group_key]['outputs'].contains(proc['outputs']))
      # we must check that the hooks have been added
      # self.assertTrue(results['proc_groups'][group_key]['hooks_into']==proc['hooks_into'])
      # self.assertTrue(results['proc_groups'][group_key]['hooks_outof']==proc['hooks_outof'])
      # we must check that the links defined have been added
      # self.assertTrue(results['proc_groups'][group_key]['links_defined'].contains(proc['links_defined']))
      # we must check that the links used have been added
      # self.assertTrue(results['proc_groups'][group_key]['links'].contains(proc['links']))


if __name__ == '__main__':
    unittest.main()