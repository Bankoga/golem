import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.base.static_comp import StaticComp
from data.enums.prop_types import CtgType

from tests.strategies.pos_strats import valid_locale, ctg_prop
from tests.strategies.prop_strats import arbitrary_id

class TestStaticComp(unittest.TestCase):
  def setUp(self):
    self.valid_id = 'TotallyValidId'
    self.valid_ctg = CtgType.FSET
    self.comp = StaticComp(self.valid_id, self.valid_ctg)
  
  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_set_invalid_id(self,itm_id):
    with self.assertRaises(ValueError):
      self.comp.set_id(itm_id)

  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_set_invalid_ctg(self,itm_id,ctg):
    with self.assertRaises(ValueError):
      self.comp.set_ctg(ctg)

  @given(arbitrary_id()) # pylint: disable=no-value-for-parameter
  def test_set_id(self, itm_id):
    self.comp.set_id(itm_id)
    self.assertEqual(self.comp.get_id(), itm_id)
  
  @given(ctg_prop()) # pylint: disable=no-value-for-parameter
  def test_set_ctg(self, ctg):
    self.comp.set_ctg(ctg)
    self.assertEqual(self.comp.get_ctg(), ctg)

  def test_get_id(self):
    self.assertEqual(self.comp.get_id(), self.valid_id)

  def test_get_ctg(self):
    self.assertEqual(self.comp.get_ctg(), self.valid_ctg)

  # @given(valid_locale()) # pylint: disable=no-value-for-parameter
  # def test_get_pos_in(self, locale):
  #   pass

  # def test_locale(self):
  #   pass

if __name__ == '__main__':
  unittest.main()