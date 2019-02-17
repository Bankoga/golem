import unittest
from hypothesis import given
from hypothesis import strategies as st
from data.axioms.configs import proc_ids,file_type
from components.procs.proc import Proc
from components.procs.proc_provider import proc_services
from utils.config_reader import read

class TestGLG(unittest.TestCase):

  def setUp(self):
    self.proc_id = proc_ids['glg']
    self.proc =  proc_services.get(self.proc_id, **{})
    self.proc_conf = read(self.proc_id,file_type['proc'])
  
  # WHAT ARE THE PROPERTIES OF THE CONF TO PROC OBJECT MAP THAT REFLECT THE SUCCESS OF THE METHOD BEING TESTED!
  def check_groups_for_property(self, conf_prop):
    if conf_prop in self.proc_conf:
      if self.proc_conf[conf_prop] is None:
        for group in self.proc.groups:
          self.assertIsNone(group[conf_prop])
      else:
        for conf_group in self.proc_conf[conf_prop]:
          if self.proc_conf[conf_prop][conf_group] is None:
              self.assertIsNone(self.proc.groups[conf_group][conf_prop])
          else:
            self.assertEqual(
              self.proc_conf[conf_prop][conf_group],
              self.proc.groups[conf_group][conf_prop]
            )
  
  def check_groups_for_hook_type(self, hook_type):
    if hook_type in self.proc_conf:
      if self.proc_conf[hook_type] is None:
        for group in self.proc.groups:
          self.assertIsNone(group[hook_type])
      else:
        for conf_group in self.proc_conf[hook_type]:
          if self.proc_conf[hook_type][conf_group] is None:
              self.assertIsNone(self.proc.groups[conf_group][hook_type])
          else:
            self.assertEqual(
              self.proc_conf[hook_type][conf_group],
              self.proc.groups[conf_group][hook_type]
            )

  def test_type_data_were_inserted_correctly(self):
    # self.assertTrue(False)
    if (self.proc_conf['type_data']['name'] is None):
      self.assertIsNone(self.proc.name)
    else:
      self.assertEqual(self.proc_conf['type_data']['name'],self.proc.name)
    
    if (self.proc_conf['type_data']['type'] is None):
      self.assertIsNone(self.proc.type)
    else:
      self.assertEqual(self.proc_conf['type_data']['type'],self.proc.type)
    
    if (self.proc_conf['type_data']['purpose'] is None):
      self.assertIsNone(self.proc.purpose)
    else:
      self.assertEqual(self.proc_conf['type_data']['purpose'],self.proc.purpose)

  def test_proc_groups_were_inserted_correctly(self):
    for conf_group in self.proc_conf['group_details']:
      self.assertDictContainsSubset(
        conf_group,
        self.proc.groups[conf_group['id']]
      )

  def test_inputs_were_inserted_correctly(self):
    conf_prop = 'inputs'
    self.check_groups_for_property(conf_prop)
  
  def test_outputs_were_inserted_correctly(self):
    conf_prop = 'outputs'
    self.check_groups_for_property(conf_prop)
  
  def test_hooks_from_were_inserted_correctly(self):
    self.check_groups_for_hook_type('hooks_outof')
  
  def test_hooks_to_were_inserted_correctly(self):
    self.check_groups_for_hook_type('hooks_to')
  
  # def test_links_defined_were_inserted_correctly(self):
  #   # we must check that the links defined have been added
  #   if (self.proc_conf['links_defined'] is None):
  #     self.assertTrue(self.proc['links_defined'] is None)
  #   else:
  #     self.assertTrue(self.proc['links_defined']== self.proc_conf['links_defined'])
  #   # we must check that the links used have been added
  
  # def test_links_used_were_inserted_correctly(self):
  #   if (self.proc_conf['links_used'] is None):
  #     self.assertTrue(self.proc['links_used'] is None)
  #   else:
  #     self.assertTrue(self.proc['links_used'] == self.proc_conf['links_used'])
  
  # def test_stage_groups_were_inserted_correctly(self):
  #   for i,stage in enumerate(self.proc['stages']):
  #     self.assertTrue(stage == (self.proc_conf['stage_to_groups_dict'][i]))
  #   # we must check that each group is created, and populated with the correct details

if __name__ == '__main__':
  unittest.main()