import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.workers.worker_comp import WorkerComp
from components.enums.pos import CtgType
from tests.components.base.test_static_comp import TestStaticComp

class TestWorkerComp(TestStaticComp):
  def setUp(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.FSET
    self.comp = WorkerComp(item_id=self.label, ctg=self.ctg)

  def test_register(self):
    with self.assertRaises(RuntimeError):
      self.comp.register()

  def test_operate(self):
    with self.assertRaises(RuntimeError):
      self.comp.operate()

if __name__ == '__main__':
  unittest.main()