import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.enums.prop_types import FieldType, ChannelType, RsrcType
from tests.strategies.channel_strats import arb_meld_str
from components.vars.meld import Meld, read_meld_str


class TestMeld(unittest.TestCase):

  def setUp(self):
    self.defaults = {
      'ch_type': ChannelType.OVERLAY,
      'resource': RsrcType.ENERGIZER,
      'address': None,
      'shape': (1,1)
    }
    self.meld = Meld()

  def test_defaults(self):
    for i,k in enumerate(self.defaults):
      self.assertEqual(self.meld[i], self.defaults[k])

  @given(arb_meld_str()) # pylint: disable=no-value-for-parameter
  def test_read_meld_str(self,meld_str):
    meld_tuple = meld_str.split(';')
    res = read_meld_str(meld_str)
    self.assertEqual(res.ch_type,meld_tuple[0])
    self.assertEqual(res.resource,meld_tuple[1])
    self.assertTrue(res.address==meld_tuple[2])
    self.assertEqual(res.shape,meld_tuple[3])

if __name__ == '__main__':
  unittest.main()
