import unittest

from hypothesis import given
from hypothesis import strategies as st

from tests.strategies.pos_strats import arb_lineage

class TestData(unittest.TestCase):

  @given(arb_lineage()) # pylint: disable=no-value-for-parameter
  def test_lineage_id(self, lineage):
    expectation = ''
    for i,field in enumerate(lineage._fields):
      if lineage[i] is None:
        break
      elif expectation == '':
        expectation = lineage[i]
      else:
        expectation = f'{expectation}-{lineage[i]}'
    self.assertEqual(str(lineage), expectation)

if __name__ == '__main__':
  unittest.main()