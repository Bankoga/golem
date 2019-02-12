import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
# from config_tests_data.py import *
from components.config_reader import read
from components.config_operations import build_full_config
from components.config_operations import build_module_entry

class TestConfigOperations(unittest.TestCase):
  def setUp(self):
    self.config = read('Test','golem')

  def test_build_full_config(self):
    self.assertTrue(False)

  def test_build_module_entry(self):
    module = self.config['Modules'][0]
    # building a module config means turning all of the properties into a single list of processing group properties ready for melding
    # thus building a module config is composed of several steps
    # first we must collect the missing proc type information from the corresponding config
    self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
