import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.func_groups.coders.coder_provider import coder_services
from data.axioms.configs import file_type, coder_ids
from data.enums.prop_types import GroupType
from tests.components.func_groups.coders.test_coder import TestCoder
from utils.config_reader import read

class TestPartsSensor(TestCoder):

  def setUp(self):
    self.coder_id = coder_ids['ps']
    self.coder =  coder_services.get(self.coder_id, **{})
    self.coder_conf = read(self.coder_id,file_type['coder'])
  
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

    if (type_obj['rsp_freq'] is None):
      self.assertIsNone(self.coder.rsp_freq)
    else:
      self.assertEqual(type_obj['rsp_freq'],self.coder.rsp_freq)

if __name__ == '__main__':
  unittest.main()