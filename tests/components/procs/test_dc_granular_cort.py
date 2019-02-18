import unittest
from hypothesis import given
from hypothesis import strategies as st
from data.axioms.configs import proc_ids,file_type
from components.procs.proc import Proc
from components.procs.proc_provider import proc_services
from utils.config_reader import read
from components.ordinators.ordinator_provider import ordinator_services

class TestGLG(unittest.TestCase):

  def setUp(self):
    self.proc_id = proc_ids['glg']
    self.proc =  proc_services.get(self.proc_id, **{})
    self.proc_conf = read(self.proc_id,file_type['proc'])
  
  # WHAT ARE THE PROPERTIES OF THE CONF TO PROC OBJECT MAP THAT REFLECT THE SUCCESS OF THE METHOD BEING TESTED!
  def check_groups_for_property(self, conf_prop):
    prop_obj = self.proc_conf[conf_prop]
    if conf_prop in self.proc_conf:
      if prop_obj is None:
        for group in self.proc.groups:
          self.assertIsNone(group[conf_prop])
      else:
        for conf_group in prop_obj:
          if prop_obj[conf_group] is None:
              self.assertIsNone(self.proc.groups[conf_group][conf_prop])
          else:
            self.assertEqual(
              prop_obj[conf_group],
              self.proc.groups[conf_group][conf_prop]
            )

  def test_type_data_were_inserted_correctly(self):
    type_obj = self.proc_conf['type_data']
    if (type_obj['name'] is None):
      self.assertIsNone(self.proc.name)
    else:
      self.assertEqual(type_obj['name'],self.proc.name)
    
    if (type_obj['type'] is None):
      self.assertIsNone(self.proc.type)
    else:
      self.assertEqual(type_obj['type'],self.proc.type)
    
    if (type_obj['purpose'] is None):
      self.assertIsNone(self.proc.purpose)
    else:
      self.assertEqual(type_obj['purpose'],self.proc.purpose)
    
    if (type_obj['ordinal_direction'] is None):
      self.assertIsNone(self.proc.ordinal_direction is None)
    else:
      self.assertEqual(type_obj['ordinal_direction'],self.proc.ordinal_direction)

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
  
  def test_hooks_were_inserted_correctly(self):
    hook_prop = 'hooks'
    if hook_prop in self.proc_conf:
      hooks = self.proc_conf[hook_prop]
      if hooks is None:
        for group in self.proc.groups:
          self.assertIsNone(group[hook_prop])
      else:
        for hook_type in hooks:
          for proc_group in hooks[hook_type]:
            self.assertIn(
              hook_type,
              self.proc.groups[proc_group][hook_prop]
            )

  def test_links_defined_were_inserted_correctly(self):
    conf_prop='links_defined'
    if (self.proc_conf[conf_prop] is None):
      self.assertTrue(self.proc.link_definitions is None)
    else:
      for link in self.proc_conf[conf_prop]:
        self.assertTrue(self.proc.link_definitions[link['id']] == link)

  def test_links_used_were_inserted_correctly(self):
    conf_prop='links_used'
    if not self.proc_conf[conf_prop]:
      self.assertFalse(self.proc.links_used)
    else:
      for link in self.proc_conf[conf_prop]:
        self.assertTrue(self.proc.links_used[link['id']] == link)
  
  def test_init_stage_data_were_inserted_correctly(self):
    conf_obj = self.proc_conf['stages_to_groups_dict']
    sz = len(conf_obj)
    for i,stage in enumerate(conf_obj):
      for group in conf_obj[i]['groups']:
        ord_to_index = ordinator_services.get(self.proc.ordinal_direction).get_ord_index(i,sz)
        self.assertEqual(self.proc.groups[group]['pos'].s, -1)
        self.assertEqual(self.proc.groups[group]['pos'].x, -1)
        self.assertEqual(self.proc.groups[group]['pos'].y, -1)
        self.assertEqual(self.proc.groups[group]['pos'].z, ord_to_index)

if __name__ == '__main__':
  unittest.main()