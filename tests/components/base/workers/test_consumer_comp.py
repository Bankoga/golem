import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.workers.consumer_comp import ConsumerComp
from components.enums.pos import CtgType
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from tests.components.base.workers.test_worker_comp import TestWorkerComp


class TestConsumerComp(TestWorkerComp):
  def setUp(self):
    self.registry = AddressRegistry(label='global_registry')
    self.address = Address(golem='a',matrix='l',func_set='b',stage='base',group='randos',packager='star_0',instruction='conv_instruct_0')
    self.label = 'conv_instruction_0'
    self.ctg = CtgType.INSTRUCTION
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.comp = ConsumerComp(label=self.label, ctg=self.ctg)

if __name__ == '__main__':
  unittest.main()