import unittest

from hypothesis import given
from hypothesis import strategies as st

from tests.strategies.packing_strats import channel_arbitrary,valid_channel_arbitrary

from utils.helpers.convoluter import get_conv_sign

class TestConvoluter(unittest.TestCase):

  @given(channel_arbitrary(),channel_arbitrary()) # pylint: disable=no-value-for-parameter
  def test_get_conv_sign_from_arbitrary(self, inp_pack, out_pack):
    if inp_pack.var is None or out_pack.var is None:
      with self.assertRaises(RuntimeError):
        get_conv_sign(inp_pack, out_pack)
    else:
      expectation = 0
      if inp_pack.var.shape < out_pack.var.shape:
        expectation = -1
      elif inp_pack.var.shape > out_pack.var.shape:
        expectation = 1
      result = get_conv_sign(inp_pack, out_pack)
      self.assertEqual(result, expectation)

  # @given(valid_channel_arbitrary()) # pylint: disable=no-value-for-parameter
  # def test_get_conv_sign_from_valid(self, inp_pack, out_pack):
  #   expectation = 0
  #   if inp_pack.var.shape > out_pack.var.shape:
  #     expectation = -1
  #   elif inp_pack.var.shape < out_pack.var.shape:
  #     expectation = 1
  #   result = get_conv_sign(inp_pack, out_pack)
  #   self.assertEqual(result, expectation)


if __name__ == '__main__':
  unittest.main()