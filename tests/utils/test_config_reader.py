import unittest
from hypothesis import given
import hypothesis.strategies as st

# from config_tests_data.py import *
from data.axioms.props import dest_key_pattern 
from utils.config_reader import read

class TestConfigReader(unittest.TestCase):

  def test_read_from_golem(self):
    config = read('Test','golem')
    self.assertTrue(config['type_data']['golem']=='Test')

  def test_read_from_proc(self):
    config =  read('GLG','proc')
    self.assertTrue(config['id']=='GLG')

if __name__ == '__main__':
    unittest.main()