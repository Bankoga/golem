import unittest
from yaml import load, dump
import unittest
from hypothesis import given
import hypothesis.strategies as st
from string import ascii_lowercase
from data.axioms.matrix import dest_key_pattern
from components.config_reader import read
from golem.core import Golem

class GolemTests(unittest.TestCase):

  def setUp(self):
    self.golem = Golem()
