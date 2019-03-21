import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.workers.producer_comp import ProducerComp
from components.enums.pos import CtgType
from components.matrix.address_registry import AddressRegistry
from components.vars.data import Address
from tests.components.base.workers.test_worker_comp import TestWorkerComp


class TestProducerComp(TestWorkerComp):
  def setUp(self):
    self.registry = AddressRegistry(label='global_registry')
    self.address = Address(golem='a',matrix='l',func_set='b',stage='base',group='randos',packager='star_0')
    self.label = 'star_0'
    self.ctg = CtgType.PACKAGER
    self.reg_item = {
      'reg_id': self.label,
      'address': self.address
    }
    self.values = [self.registry]
    self.var = tuple(self.values)
    self.comp = ProducerComp(label=self.label, ctg=self.ctg)
    self.comp.build(*self.values)

if __name__ == '__main__':
  unittest.main()