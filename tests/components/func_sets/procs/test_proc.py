import unittest
from hypothesis import given
from hypothesis import strategies as st
from data.axioms.configs import proc_ids,file_type
from data.enums.prop_types import SetType
from components.func_sets.procs.proc import Proc
from components.func_sets.procs.proc_provider import proc_services
from utils.config_reader import read
from utils.cardinators.cardinator_provider import cardinator_services

class TestProc(unittest.TestCase):

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
      self.assertIsNone(self.proc.ctg_type)
    else:
      self.assertEqual(SetType[type_obj['type']],self.proc.ctg_type)
    
    if (type_obj['purpose'] is None):
      self.assertIsNone(self.proc.purpose)
    else:
      self.assertEqual(type_obj['purpose'],self.proc.purpose)
    
    if (type_obj['cardinal_direction'] is None):
      self.assertIsNone(self.proc.cardinal_direction is None)
    else:
      self.assertEqual(type_obj['cardinal_direction'],self.proc.cardinal_direction)

  def test_proc_groups_were_inserted_correctly(self):
    for conf_group in self.proc_conf['group_details']:
      self.assertDictContainsSubset(
        conf_group,
        self.proc.groups[conf_group['id']]
      )

  def test_outputs_were_inserted_correctly(self):
    conf_prop = 'outputs'
    self.check_groups_for_property(conf_prop)
  
  def test_init_stage_data_were_inserted_correctly(self):
    conf_obj = self.proc_conf['stages_to_groups_dict']
    sz = len(conf_obj)
    for i,stage in enumerate(conf_obj):
      for group in conf_obj[i]['groups']:
        ord_to_index = cardinator_services.get(self.proc.cardinal_direction).get_card_index(i,sz)
        self.assertEqual(self.proc.groups[group]['pos'].s, -1)
        self.assertEqual(self.proc.groups[group]['pos'].x, -1)
        self.assertEqual(self.proc.groups[group]['pos'].y, -1)
        self.assertEqual(self.proc.groups[group]['pos'].z, ord_to_index)

  def test_process_inputs(self, input_set):
    """
    what are the assumptions we make as part of testing inputs to a proc group?
    What happens if these assumptions are violated?
    """

  # @given(module_input_set(st.just(set_ids['glg']))) # pylint: disable=no-value-for-parameter
  # def test_process_inputs(self):
  #   # in the beginning, we have a list of unordered, and unaggregated inputs
  #   pass

if __name__ == '__main__':
  unittest.main()