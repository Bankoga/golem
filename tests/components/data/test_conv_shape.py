import unittest

from hypothesis import given
from hypothesis import strategies as st

from tests.strategies.packing_strats import valid_conv_shape

from components.data.conv_shape import ConvShape

from numpy import ones, array_equal

from tests.strategies.packing_strats import valid_resource_data

class TestConvShape(unittest.TestCase):

  def setUp(self):
    self.f_shape = (4,4)
    self.s_shape = (1,1)
    self.comp = ConvShape(self.f_shape,self.s_shape)

  def test_init(self):
    self.assertEqual(self.comp.f_shape,self.f_shape)
    self.assertEqual(self.comp.s_shape,self.s_shape)
    expectation = ones(self.f_shape)
    result = self.comp.weights
    self.assertTrue(array_equal(result, expectation))

  @given(valid_resource_data()) # pylint: disable=no-value-for-parameter
  def test_conv(self, npmatrix):
    # TODO: Build a valid package for a specific id strategy
    """ what needs to be considered when applying a conv to an arbitrary matrix?
        these are all part of the conv considerations
        what about size mismatches between regions?
        which index do we center on? the source index
        Where do the weights reside? with the conv shape
        Where is activity tracked for plasticity? inside the instruction
    """
    result = self.comp.conv(npmatrix)
    expectation = 0
    self.assertEqual(result,expectation)

  # @given(st.lists(valid_conv_shape())) # pylint: disable=no-value-for-parameter
  # def test_set_up_weights(self,conv_shapes):
  #   weights = self.cs.set_up_weights(conv_shapes)
  #   for shape in conv_shapes:
  #     self.assertEqual(result.shape, expectation.shape)
  #     self.assertTrue(array_equal(result, expectation))

if __name__ == '__main__':
  unittest.main()