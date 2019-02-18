# import unittest
# from hypothesis import given
# from hypothesis import strategies as st
# from data.axioms.configs import sensor_ids,file_type
# from components.sensors.sensor import Proc
# from components.sensors.sensor_provider import sensor_services
# from utils.config_reader import read
# from components.ordinators.ordinator_provider import ordinator_services

# class TestProc(unittest.TestCase):

#   def setUp(self):
#     self.sensor_id = sensor_ids['ps']
#     self.sensor =  sensor_services.get(self.sensor_id, **{})
#     self.sensor_conf = read(self.sensor_id,file_type['sensor'])
  
#   # WHAT ARE THE PROPERTIES OF THE CONF TO PROC OBJECT MAP THAT REFLECT THE SUCCESS OF THE METHOD BEING TESTED!
#   def check_groups_for_property(self, conf_prop):
#     prop_obj = self.sensor_conf[conf_prop]
#     if conf_prop in self.sensor_conf:
#       if prop_obj is None:
#         for group in self.sensor.groups:
#           self.assertIsNone(group[conf_prop])
#       else:
#         for conf_group in prop_obj:
#           if prop_obj[conf_group] is None:
#               self.assertIsNone(self.sensor.groups[conf_group][conf_prop])
#           else:
#             self.assertEqual(
#               prop_obj[conf_group],
#               self.sensor.groups[conf_group][conf_prop]
#             )

#   def test_type_data_were_inserted_correctly(self):
#     type_obj = self.sensor_conf['type_data']
#     if (type_obj['name'] is None):
#       self.assertIsNone(self.sensor.name)
#     else:
#       self.assertEqual(type_obj['name'],self.sensor.name)
    
#     if (type_obj['type'] is None):
#       self.assertIsNone(self.sensor.type)
#     else:
#       self.assertEqual(type_obj['type'],self.sensor.type)
    
#     if (type_obj['purpose'] is None):
#       self.assertIsNone(self.sensor.purpose)
#     else:
#       self.assertEqual(type_obj['purpose'],self.sensor.purpose)
    
#     if (type_obj['ordinal_direction'] is None):
#       self.assertIsNone(self.sensor.ordinal_direction is None)
#     else:
#       self.assertEqual(type_obj['ordinal_direction'],self.sensor.ordinal_direction)

#   def test_sensor_groups_were_inserted_correctly(self):
#     for conf_group in self.sensor_conf['group_details']:
#       self.assertDictContainsSubset(
#         conf_group,
#         self.sensor.groups[conf_group['id']]
#       )

#   def test_inputs_were_inserted_correctly(self):
#     conf_prop = 'inputs'
#     self.check_groups_for_property(conf_prop)
  
#   def test_outputs_were_inserted_correctly(self):
#     conf_prop = 'outputs'
#     self.check_groups_for_property(conf_prop)
  
#   def test_hooks_were_inserted_correctly(self):
#     hook_prop = 'hooks'
#     if hook_prop in self.sensor_conf:
#       hooks = self.sensor_conf[hook_prop]
#       if hooks is None:
#         for group in self.sensor.groups:
#           self.assertIsNone(group[hook_prop])
#       else:
#         for hook_type in hooks:
#           for sensor_group in hooks[hook_type]:
#             self.assertIn(
#               hook_type,
#               self.sensor.groups[sensor_group][hook_prop]
#             )

#   def test_links_defined_were_inserted_correctly(self):
#     conf_prop='links_defined'
#     if (self.sensor_conf[conf_prop] is None):
#       self.assertFalse(self.sensor.link_definitions)
#     else:
#       for link in self.sensor_conf[conf_prop]:
#         self.assertTrue(self.sensor.link_definitions[link['id']] == link)

#   def test_links_used_were_inserted_correctly(self):
#     conf_prop='links_used'
#     if not self.sensor_conf[conf_prop]:
#       self.assertFalse(self.sensor.links_used)
#     else:
#       for link in self.sensor_conf[conf_prop]:
#         self.assertTrue(self.sensor.links_used[link['id']] == link)
  
#   def test_init_stage_data_were_inserted_correctly(self):
#     conf_obj = self.sensor_conf['stages_to_groups_dict']
#     sz = len(conf_obj)
#     for i,stage in enumerate(conf_obj):
#       for group in conf_obj[i]['groups']:
#         ord_to_index = ordinator_services.get(self.sensor.ordinal_direction).get_ord_index(i,sz)
#         self.assertEqual(self.sensor.groups[group]['pos'].s, -1)
#         self.assertEqual(self.sensor.groups[group]['pos'].x, -1)
#         self.assertEqual(self.sensor.groups[group]['pos'].y, -1)
#         self.assertEqual(self.sensor.groups[group]['pos'].z, ord_to_index)

# if __name__ == '__main__':
#   unittest.main()