# import unittest
# from hypothesis import given
# from hypothesis import strategies as st
# from data.axioms.configs import proc_ids,file_type
# from components.procs.proc import Proc
# from components.procs.proc_provider import proc_services
# from utils.config_reader import read

# class TestProc(unittest.TestCase):

#   def setUp(self, proc_id='glg'):
#     self.proc_id = proc_ids[proc_id]
#     self.proc =  proc_services.get(self.proc_id, **{})
#     self.proc_conf = read(self.proc_id,file_type['proc'])

#   def test_type_data_were_inserted_correctly(self):
#     self.assertTrue(False)
#     if (self.proc_conf['type_data']['name'] is None):
#       self.assertIsNone(self.proc['name'])
#     else:
#       self.assertEqual(self.proc_conf['type_data']['name'],self.proc['name'])
    
#     if (self.proc_conf['type_data']['type'] is None):
#       self.assertIsNone(self.proc['type'])
#     else:
#       self.assertEqual(self.proc_conf['type_data']['type'],self.proc['type'])
    
#     if (self.proc_conf['type_data']['purpose'] is None):
#       self.assertIsNone(self.proc['purpose'])
#     else:
#       self.assertEqual(self.proc_conf['type_data']['purpose'],self.proc['purpose'])

# if __name__ == '__main__':
#   unittest.main()