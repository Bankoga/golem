import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.mechanisms.cogs.consumer import Consumer
from components.enums.pos import CtgType
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from tests.components.base.mechanisms.test_mechanism import TestMechanism


class TestConsumer(TestMechanism):
  def setUp(self):
    self.registry = AddressRegistry(label='global_registry')
    self.address = Address(golem='a',matrix='l',func_set='b',stage='base',group='randos',packager='star_0',instruction='conv_instruct_0')
    self.label = 'conv_instruction_0'
    self.ctg = CtgType.INSTRUCTION
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.values = [self.registry]
    self.var = tuple(self.values)
    self.comp = Consumer(label=self.label, ctg=self.ctg)
    self.comp.build(*self.values)

if __name__ == '__main__':
  unittest.main()