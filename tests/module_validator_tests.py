import unittest
from hypothesis import *
from module_validator.py import *
from string import ascii_lowercase
from .context import validators.module_validator
# from config_tests_data.py import *

class ModuleValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = ModuleValidator()

    def test_input_melds_validation(self):
        self.assertTrue(self.validator.input_melds_validation())
    def test_func_type_validation(self):
        self.assertTrue(self.validator.func_type_validation())
    def test_proc_stage_groups_dict_validation(self):
        self.assertTrue(self.validator.proc_stage_groups_dict_validation())
    def test_proc_stage_shape_validation(self):
        self.assertTrue(self.validator.proc_stage_shape_validation())
    def test_proc_group_input_melds_validation(self):
        self.assertTrue(self.validator.proc_group_input_melds_validation())
    def test_proc_group_details_validation(self):
        self.assertTrue(self.validator.proc_group_details_validation())
    def test_proc_group_output_melds_validation(self):
        self.assertTrue(self.validator.proc_group_output_melds_validation())
    def test_proc_output_melds_validation(self):
        self.assertTrue(self.validator.proc_output_melds_validation())
    def test_shape_composition_validation(self):
        self.assertTrue(self.validator.shape_composition_validation())
    def test_output_melds_validation(self):
        self.assertTrue(self.validator.output_melds_validation())
    def test_link_melds_validation(self):
        self.assertTrue(self.validator.link_melds_validation())
    def test_links_defined_validation(self):
        self.assertTrue(self.validator.links_defined_validation())


if __name__ == "__main__":
    unittest.main()