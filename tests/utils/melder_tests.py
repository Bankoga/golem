import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils import melder as Melder
from string import ascii_lowercase
# from config_tests_data.py import *

# It is an open question as to whether or not links need to be defined as part of the proc group

class MelderTests(unittest.TestCase):
  def setUp(self):
    self.melder = Melder()
  
  def test_

  def test_eval_description(self):
    self.assertTrue(False)

  def test_eval_proto_melds(self):
    self.assertTrue(False)

  def test_eval_melds(self):
    """given a list of meld templates, and WHAT DATA IS REQ?
    When the full list of melds is evaluated
    Then <count> results should be in the <format>"""
    self.assertTrue(False)
"""
Every data bearing connection between two components (modules, nodes, or otherwise) is a Meld.
All melds have the same overall full format, with several definitional formats.
A melder object can be used to do the following:
- convert descriptions of melds, into lists of proto-melds
- convert a destination pattern into a a list of proto-melds
- convert a list of proto-melds into full melds

- Full: Module_key-subdest,Resource_type,Field_shape
- Definition_A: Link_key,Resource_types

Each link type can have it's own field shape that needs to be accounted for, and each link must be counted separately so we have to dynamically generate all link input and output melds anywhere a link id is specified



"""