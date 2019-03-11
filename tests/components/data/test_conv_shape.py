import unittest

from hypothesis import given
from hypothesis import strategies as st

from tests.components.base.test_passive_comp import TestPassiveComp
from tests.strategies.packing_strats import valid_conv_shape

from components.data.conv_shape import ConvShape

from data.enums.pos import CtgType

from utils.pos import Pos

from numpy import ones, array_equal

from tests.strategies.packing_strats import valid_resource_data

class TestConvShape(TestPassiveComp):

  def setUp(self):
    self.f_shape = (4,4)
    self.s_shape = (1,1)
    self.r = 5
    self.c = 5
    self.pos = Pos(CtgType.DATA,r=self.r,c=self.c)
    self.item_id = 'TotallyValidId'
    self.comp = ConvShape(self.item_id,self.pos,self.f_shape,self.s_shape)

  # def test_init(self):
  #   self.assertEqual(self.comp.f_shape,self.f_shape)
  #   self.assertEqual(self.comp.s_shape,self.s_shape)
  #   expectation = ones(self.f_shape)
  #   result = self.comp.var
  #   self.assertTrue(array_equal(result, expectation))

  @given(st.one_of(st.text(),st.integers(),st.lists(st.integers())))
  def test_set_var(self, new_var):
    # var = {
    #   'pos': pos,
    #   'f_shape': f_shape,
    #   's_shape': s_shape,
    #   'weights': ones(f_shape)
    # }
    self.comp.set_var(new_var)
    self.assertEqual(self.comp.get_var(), new_var)

  def test_get_var(self):
    self.assertEqual(self.comp.get_var(), self.var)


  # @given(st.lists(valid_conv_shape())) # pylint: disable=no-value-for-parameter
  # def test_set_up_weights(self,conv_shapes):
  #   weights = self.cs.set_up_weights(conv_shapes)
  #   for shape in conv_shapes:
  #     self.assertEqual(result.shape, expectation.shape)
  #     self.assertTrue(array_equal(result, expectation))

if __name__ == '__main__':
  unittest.main()