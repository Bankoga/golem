import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
# from config_tests_data.py import *
from data.axioms.matrix import dest_key_pattern
from components.config_reader import read

class ConfigReaderTests(unittest.TestCase):

  def test_read_from_golem(self):
    config = read('Test','golem')
    self.assertTrue(config['TypeData']['Id']=='Test')

  def test_read_from_proc(self):
    config =  read('GLG','proc')
    self.assertTrue(config['Id']=='GLG')

  @given(st.text())
  def test_invalid_proc_attempt(self, proctype):
    self.assertWarns(FileNotFoundError, read, proctype, 'proc')