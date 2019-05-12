import unittest
from yaml import load, dump
import unittest
from hypothesis import given
import hypothesis.strategies as st

from components.axioms.props import dest_key_pattern 
from utils.config_reader import read
from golem import Golem

class TestGolem(unittest.TestCase):

  def setUp(self):
    self.golem = Golem()

if __name__ == '__main__':
    unittest.main()