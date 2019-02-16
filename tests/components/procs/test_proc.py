import unittest
from hypothesis import given
from hypothesis import strategies as st
from string import ascii_lowercase
from data.axioms.pos_maps import package_map, pipeline_map
from data.axioms.configs import proc_ids,file_type
from data.axioms.configs import procs
from components.procs.proc import Proc
from components.procs.proc_provider import proc_services
from utils.config_reader import read

# def _check_results_contains_property_from_parts_(self, result, prop, part):
#   if (part[prop] is None):
#     self.assertTrue(result[prop] is None)
#   else:
#     self.assertTrue(result[prop].contains(part[prop]))


class TestProc(unittest.TestCase):
  def __init__(self,proc_id='glg'):
    super.__init__()
    self.proc_id = proc_id[proc_id]

  def setUp(self):
    self.proc =  proc_services.get(self.proc_id, **{})
    self.proc_conf = read(self.proc_id,file_type['proc'])

  def _check_group_conf_prop_(self, conf_prop, proc_prop):
    if self.proc_conf[conf_prop] is None:
      for group in self.proc[proc_prop]:
        self.assertIsNone(group[conf_prop])
    else:
      for conf_group in self.proc_conf[conf_prop]:
        self.assertEqual(
          conf_group[conf_prop],
          self.proc[proc_prop][conf_group['id']]
        )

  """
   WHAT ARE THE PROPERTIES OF THE CONF TO PROC OBJECT MAP THAT REFLECT THE SUCCESS OF THE METHOD BEING TESTED!
  """
  def test_inputs_were_inserted_correctly(self):
    conf_prop = 'inputs'
    proc_prop = 'proc_groups'
    self._check_group_conf_prop_(conf_prop,proc_prop)
  
  # def test_outputs_were_inserted_correctly(self):
  #   for i,group_key in enumerate(self.proc['proc_groups']):
  #     # we must check that the outputs have been added
  #     if self.proc['outputs'] is not None:
  #       self.assertTrue(all(elem in self.proc['outputs'] for elem in self.proc['outputs']))
  #     for i,out_key in enumerate(self.proc_conf['outputs']):
  #       if self.proc_conf['outputs'][out_key] is not None:
  #         self.assertTrue(all(elem in self.proc['outputs'] for elem in self.proc_conf['outputs'][out_key]))
  
  # def test_hooks_from_were_inserted_correctly(self):
  #   if ('hooks_outof' in self.proc_conf):
  #     self.assertTrue(self.proc['hooks_outof']==self.proc_conf['hooks_outof'])
  #   else:
  #     self.assertTrue(self.proc['hooks_outof'] is None)
  
  # def test_hooks_to_were_inserted_correctly(self):
  #   # we must check that the hooks have been added
  #   if ('hooks_into' in self.proc_conf):
  #     self.assertTrue(self.proc['hooks_into']==self.proc_conf['hooks_into'])
  #   else:
  #     self.assertTrue(self.proc['hooks_into'] is None)
  
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