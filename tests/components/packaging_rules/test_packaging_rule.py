import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.packaging_rules.packaging_rule import PackagingRule

class TestPackagingRule(unittest.TestCase):
  def setUp(self):
    self.rule = PackagingRule()