import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packaging_rules.cells.cell import Cell
from data.axioms.enums import RuleType

class TestCell(unittest.TestCase):
  def setUp(self):
    self.rule = Cell()
  
  def test_base_rule(self):
    self.assertEqual(self.rule.type, RuleType.CELL)