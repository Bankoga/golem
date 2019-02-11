import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils.datapack import *
from string import ascii_lowercase
# from config_tests_data.py import *
from data.axioms.matrix import dest_key_pattern
from components.config_reader import ConfigReader
from data.axioms.configs import files
class ConfigReaderTests(unittest.TestCase):

  def setUp(self):
    self.reader = ConfigReader()

  def test_read_from_golem(self):
    # paths['tests']
    given a golem path
    when it is read
    then the output should match expectations
    self.reader.read(files['test.golem'])
    return False

  def test_read_from_proc(self):
    self.reader.read(files['testgate.proc'])
    return False

  def test_get_reader(self):
    return False