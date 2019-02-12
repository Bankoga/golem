import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
from validators.module_validator import ModuleValidator
from data.axioms.matrix import proc_types
# from config_tests_data.py import *

class TestModuleValidator(unittest.TestCase):
    def setUp(self):
        self.validator = ModuleValidator()

    @given(st.tuples())
    def test_input_melds_validation(self):
        isValid = self.validator.input_melds_validation()
        self.assertTrue(isValid)


    def test_proc_type_validation(self,proc_type):
        isValid = self.validator.proc_type_validation(proc_type)
        self.assertTrue(isValid)
        self.assertIn(proc_type,proc_types)
    
    
    def test_proc_stage_groups_dict_validation(self):
        isValid = self.validator.proc_stage_groups_dict_validation()
        self.assertTrue(isValid)
    
    
    def test_proc_stage_shape_validation(self):
        isValid = self.validator.proc_stage_shape_validation()
        self.assertTrue(isValid)
    
    
    def test_proc_group_input_melds_validation(self):
        isValid = self.validator.proc_group_input_melds_validation()
        self.assertTrue(isValid)
    
    
    def test_proc_group_details_validation(self):
        isValid = self.validator.proc_group_details_validation()
        self.assertTrue(isValid)
    
    
    def test_proc_group_output_melds_validation(self):
        isValid = self.validator.proc_group_output_melds_validation()
        self.assertTrue(isValid)
    
    
    def test_proc_output_melds_validation(self):
        isValid = self.validator.proc_output_melds_validation()
        self.assertTrue(isValid)
    
    
    def test_shape_composition_validation(self):
        isValid = self.validator.shape_composition_validation()
        self.assertTrue(isValid)
    
    
    def test_output_melds_validation(self):
        isValid = self.validator.output_melds_validation()
        self.assertTrue(isValid)
    
    
    def test_link_melds_validation(self):
        isValid = self.validator.link_melds_validation()
        self.assertTrue(isValid)
    
    
    def test_links_defined_validation(self):
        isValid = self.validator.links_defined_validation()
        self.assertTrue(isValid)



if __name__ == '__main__':
    unittest.main()