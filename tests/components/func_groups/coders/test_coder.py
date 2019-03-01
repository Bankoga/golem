import unittest
from hypothesis import given
from hypothesis import strategies as st
from data.axioms.configs import coder_ids,file_type
from data.enums.prop_types import GroupType
from components.func_groups.coders.coder import Coder
from components.func_groups.coders.coder_provider import coder_services
from utils.config_reader import read
from utils.cardinators.cardinator_provider import cardinator_services

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
          self.assertFalse(self.coder.groups[group][conf_prop])
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
      self.assertEqual(GroupType[type_obj['type']],self.coder.type)
    
    if (type_obj['purpose'] is None):
      self.assertIsNone(self.coder.purpose)
    else:
      self.assertEqual(type_obj['purpose'],self.coder.purpose)

  def test_coder_groups_were_inserted_correctly(self):
    conf_obj = self.coder_conf['groups']
    for i,group in enumerate(conf_obj):
    # for group in self.coder_conf['group_details']:
      self.assertDictContainsSubset(
        group,
        self.coder.groups[group['id']]
      )
      self.assertEqual(self.coder.groups[group['id']]['pos'].s, -1)
      self.assertEqual(self.coder.groups[group['id']]['pos'].x, -1)
      self.assertEqual(self.coder.groups[group['id']]['pos'].y, -1)
      self.assertEqual(self.coder.groups[group['id']]['pos'].z, 0)

  def test_outputs_were_inserted_correctly(self):
    conf_prop = 'outputs'
    self.check_groups_for_property(conf_prop)
  
  def test_hooks_were_inserted_correctly(self):
    hook_prop = 'hooks'
    if hook_prop in self.coder_conf:
      hooks = self.coder_conf[hook_prop]
      if hooks is None:
        for group in self.coder.groups:
          self.assertFalse(self.coder.groups[group][hook_prop])
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

if __name__ == '__main__':
  unittest.main()