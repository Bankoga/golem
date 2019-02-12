import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
# from config_tests_data.py import *
from components.config_reader import read

class DataPackTests(unittest.TestCase):

  def test_build_full_config(self):
    golem_config = read('Test','golem')