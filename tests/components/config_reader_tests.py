import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils.datapack import *
from string import ascii_lowercase
# from config_tests_data.py import *
from data.axioms.matrix import dest_key_pattern
from components.config_reader import ConfigReader
reader = ConfigReader()
cfg = reader.read('Test','golem')

class ConfigReaderTests(unittest.TestCase):

  def setUp(self):
    self.reader = ConfigReader()

  def test_read_from_golem(self):
    config = self.reader.read('Test','golem')
    self.assertTrue(config['TypeData']['Id']=='Test')

  def test_read_from_proc(self):
    config =  self.reader.read('TestGate','proc')
    self.assertTrue(config['Id']=='TestGate')