import unittest
from hypothesis import given
from hypothesis import strategies as st
from data.axioms.configs import coder_ids,file_type
from components.coders.coder import Proc
from components.coders.coder_provider import coder_services
from utils.config_reader import read
from components.ordinators.ordinator_provider import ordinator_services

class TestCoder(unittest.TestCase):

  def setUp(self):
    self.coder_id = coder_ids['ps']
    self.coder =  coder_services.get(self.coder_id, **{})
    self.coder_conf = read(self.coder_id,file_type['coder'])
  
  # WHAT ARE THE PROPERTIES OF THE CONF TO PROC OBJECT MAP THAT REFLECT THE SUCCESS OF THE METHOD BEING TESTED!
  def check_groups_for_property(self, conf_prop):
    prop_obj = self.coder_conf[conf_prop]
    if conf_prop in self.coder_conf:
      if prop_obj is None:
        for group in self.coder.groups:
          self.assertIsNone(group[conf_prop])
      else:
        for conf_group in prop_obj:
          if prop_obj[conf_group] is None:
              self.assertIsNone(self.coder.groups[conf_group][conf_prop])
          else:
            self.assertEqual(
              prop_obj[conf_group],
              self.coder.groups[conf_group][conf_prop]
            )

  def test_type_data_were_inserted_correctly(self):
    type_obj = self.coder_conf['type_data']
    if (type_obj['name'] is None):
      self.assertIsNone(self.coder.name)
    else:
      self.assertEqual(type_obj['name'],self.coder.name)
    
    if (type_obj['type'] is None):
      self.assertIsNone(self.coder.type)
    else:
      self.assertEqual(type_obj['type'],self.coder.type)
    
    if (type_obj['purpose'] is None):
      self.assertIsNone(self.coder.purpose)
    else:
      self.assertEqual(type_obj['purpose'],self.coder.purpose)
    
    if (type_obj['ordinal_direction'] is None):
      self.assertIsNone(self.coder.ordinal_direction is None)
    else:
      self.assertEqual(type_obj['ordinal_direction'],self.coder.ordinal_direction)

  def test_coder_groups_were_inserted_correctly(self):
    for conf_group in self.coder_conf['group_details']:
      self.assertDictContainsSubset(
        conf_group,
        self.coder.groups[conf_group['id']]
      )

  def test_inputs_were_inserted_correctly(self):
    conf_prop = 'inputs'
    self.check_groups_for_property(conf_prop)
  
  def test_outputs_were_inserted_correctly(self):
    conf_prop = 'outputs'
    self.check_groups_for_property(conf_prop)
  
  def test_hooks_were_inserted_correctly(self):
    hook_prop = 'hooks'
    if hook_prop in self.coder_conf:
      hooks = self.coder_conf[hook_prop]
      if hooks is None:
        for group in self.coder.groups:
          self.assertIsNone(group[hook_prop])
      else:
        for hook_type in hooks:
          for coder_group in hooks[hook_type]:
            self.assertIn(
              hook_type,
              self.coder.groups[coder_group][hook_prop]
            )

  def test_links_defined_were_inserted_correctly(self):
    conf_prop='links_defined'
    if (self.coder_conf[conf_prop] is None):
      self.assertFalse(self.coder.link_definitions)
    else:
      for link in self.coder_conf[conf_prop]:
        self.assertTrue(self.coder.link_definitions[link['id']] == link)

  def test_links_used_were_inserted_correctly(self):
    conf_prop='links_used'
    if not self.coder_conf[conf_prop]:
      self.assertFalse(self.coder.links_used)
    else:
      for link in self.coder_conf[conf_prop]:
        self.assertTrue(self.coder.links_used[link['id']] == link)
  
  def test_init_stage_data_were_inserted_correctly(self):
    conf_obj = self.coder_conf['stages_to_groups_dict']
    sz = len(conf_obj)
    for i,stage in enumerate(conf_obj):
      for group in conf_obj[i]['groups']:
        ord_to_index = ordinator_services.get(self.coder.ordinal_direction).get_ord_index(i,sz)
        self.assertEqual(self.coder.groups[group]['pos'].s, -1)
        self.assertEqual(self.coder.groups[group]['pos'].x, -1)
        self.assertEqual(self.coder.groups[group]['pos'].y, -1)
        self.assertEqual(self.coder.groups[group]['pos'].z, ord_to_index)

if __name__ == '__main__':
  unittest.main()