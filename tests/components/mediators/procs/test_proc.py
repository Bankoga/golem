import unittest

from hypothesis import given, reproduce_failure
from hypothesis import strategies as st
from numpy import append, array

from components.axioms.configs import file_type, proc_ids, set_ids
from components.enums.prop_types import ChannelType, ModuleType
from components.mediators.procs.proc import Proc
from components.mediators.procs.proc_provider import proc_services
from tests.components.mediators.test_module import TestModule
from tests.strategies.module_strats import (group_input_set, module_input_set,
                                            unbuilt_module_input_set)
from utils.cardinators.cardinator_provider import cardinator_services
from utils.config_reader import read
from utils.misc import heapsort


class TestProc(TestModule):

  def setUp(self):
    self.proc_id = proc_ids['glg']
    self.proc =  proc_services.get(self.proc_id, **{})
    self.proc_conf = read(self.proc_id,file_type['proc'])
    self.proc.build()
  
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
      self.assertEqual(ModuleType[type_obj['type']],self.proc.ctg_type)
    
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

  # def test_reset_weights(self):
  #   with self.assertRaises(NotImplementedError):
  #     self.proc.reset_weights()
  #   # iterate through all weights in the proc
  #   # TODO: HOW do we iterate through all weights in the proc

  # @given(glg_input_set())  # pylint: disable=no-value-for-parameter
  # def test_process_unbuilt_inputs(self, inputs):
  #   # this should raise a runtime error
  #   with self.assertRaises(RuntimeError):
  #     self.proc.process_inputs(inputs)

  # def test_process_no_inputs(self):
  #   #  this seems like it should be a valid case
  #   # given an arbitrary proc group, we may not get data to process this time step
  #   pass

  # @given(module_input_set(st.just(set_ids['glg'])),group_input_set(st.just(set_ids['glg']))) # pylint: disable=no-value-for-parameter
  @given(module_input_set(st.just(set_ids['glg'])))# pylint: disable=no-value-for-parameter
  def test_process_inputs(self, module_inputs):
    """
    what are the assumptions we make as part of testing inputs to a proc group?
    - every item in the input set has already been built
    - the proc has been built
    - inputs exist?
    - the inputs arrive unsorted, and unaggregated
    The first three are test cases, The fourth relates to input validity
    What are the properties of valid inputs to a func set?
    - The func set or one of its groups is listed as the recipient
    - Do we assume that we get new data? Do we assume that all groups in the func set have at least one dedicated input?
    """
    
    input_set = module_inputs
    expectation = []
    results = self.proc.process_inputs(input_set)
    expectation = {}
    for pack in input_set:
      p_type = pack.get_ctg()
      if p_type in expectation:
        expectation[p_type].append(pack)
      else:
        expectation[p_type] = [pack]
    if ChannelType.AGGREGATE in expectation:
      expectation[ChannelType.AGGREGATE] = heapsort(expectation[ChannelType.AGGREGATE])
      agg = None
      for pack in expectation[ChannelType.AGGREGATE]:
        if agg is None:
          agg = pack.var
        else:
          append(agg, pack.var)
      expectation[ChannelType.AGGREGATE] = agg
    self.assertEqual(results, expectation)


if __name__ == '__main__':
  unittest.main()
