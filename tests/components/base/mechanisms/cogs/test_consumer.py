import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.mechanisms.cogs.consumer import Consumer
from components.enums.pos import CtgType
from components.matrix.lineage_registry import LineageRegistry
from components.vars.data import Lineage
from tests.components.base.mechanisms.test_mechanism import TestMechanism


class TestConsumer(TestMechanism):
  def set_up_base(self):
    self.label = 'collector_0'
    self.ctg = CtgType.INSTRUCTION
    self.comp_class = Consumer

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_registry')
    self.lineage = Lineage(golem='a',matrix='l',func_set='b',stage='base',group='randos',packager='star_0',instruction='conv_instruct_0')
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.values = [self.registry]
    self.var = tuple(self.values)

  def setUp(self):
    self.set_up_base()
    self.set_up_var()
    self.comp = self.comp_class(*self.values,label=self.label, ctg=self.ctg)

if __name__ == '__main__':
  unittest.main()