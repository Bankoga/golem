import unittest

from hypothesis import given
from hypothesis import strategies as st

from tests.strategies.packing_strats import valid_datapack_arbitrary

from utils.helpers.convoluter import get_conv_sign

class TestConvoluter(unittest.TestCase):

  @given(valid_datapack_arbitrary()) # pylint: disable=no-value-for-parameter
  def test_get_conv_sign_from_arbitrary(self, inp_shape, out_shape):
    if not inp_shape or not out_shape:
      with self.assertRaises(ValueError):
        get_conv_sign(inp_shape, out_shape)
    expectation = 0
    if inp_shape > out_shape:
      expectation = -1
    elif inp_shape < out_shape:
      expectation = 1
    result = get_conv_sign(inp_shape, out_shape)
    self.assertEqual(result, expectation)

  @given(valid_datapack_arbitrary()) # pylint: disable=no-value-for-parameter
  def test_get_conv_sign_from_valid(self, inp_shape, out_shape):
    expectation = 0
    if inp_shape > out_shape:
      expectation = -1
    elif inp_shape < out_shape:
      expectation = 1
    result = get_conv_sign(inp_shape, out_shape)
    self.assertEqual(result, expectation)


if __name__ == '__main__':
  unittest.main()