import unittest

from hypothesis import given
from hypothesis import strategies as st

from tests.strategies.pos_strats import arb_addr

class TestData(unittest.TestCase):

  @given(arb_addr()) # pylint: disable=no-value-for-parameter
  def test_address_id(self, addr):
    expectation = ''
    for i,field in enumerate(addr._fields):
      if addr[i] is None:
        break
      elif expectation == '':
        expectation = addr[i]
      else:
        expectation = f'{expectation}-{addr[i]}'
    self.assertEqual(str(addr), expectation)

if __name__ == '__main__':
  unittest.main()