import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, array_equal, ones

from components.vars.data import Address
from components.data.collector_segment import CollectorSegment
from components.enums.pos import CtgType
from tests.components.base.test_plastic_comp import TestPlasticComp
from tests.strategies.data_strats import valid_resource_data, valid_shape, valid_weights
from utils.pos import Pos
from tests.strategies.pos_strats import arb_addr
from tests.components.base.test_segment import TestSegment

class TestCollectorSegment(TestPlasticComp,TestSegment):
  def set_up_base(self):
    self.ctg = CtgType.DATA
    self.label = 'dend_abov_a_segment_2'
    
  def set_up_var(self):
    self.address = Address(golem='a',matrix='l',func_set='glg', stage='prim', group='assoc_from', packager='star_0', instruction='dend_above_a')
    self.source_index = (0,0)
    self.fill_shape = (4,4)
    self.weights = ones(self.fill_shape)
    self.values = []
    self.var = tuple(self.values)

  def set_up_defaults(self):
    self.default_shape = (4,4)
    self.default_weights = ones(self.default_shape)
    self.default_num_dim_of_mass = len(self.default_shape)
    self.default_is_locked = False

  def set_up_dynamic_props(self):
    self.baseline = self.values

  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.set_up_var()
    self.set_up_dynamic_props()
    self.comp = CollectorSegment(address=self.address,source_index=self.source_index,fill_shape=self.fill_shape,label=self.label)

  @given(arb_addr(), valid_shape(), valid_shape()) # pylint: disable=no-value-for-parameter
  def test_prepare_var_args(self, address, source_index, f_shape):
    var_kwargs = {'address':address, 'source_index':source_index, 'fill_shape':f_shape}
    expectation = tuple([])
    result = self.comp.prepare_var_args(**var_kwargs)
    self.assertEqual(result, expectation)
    self.assertEqual(self.comp.shape, var_kwargs['fill_shape'])


if __name__ == '__main__':
  unittest.main()
