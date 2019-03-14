import unittest

from hypothesis import given
from hypothesis import strategies as st

from tests.components.base.test_passive_comp import TestPassiveComp

from components.enums.pos import CtgType

from utils.pos import Pos

class TestLocale(TestPassiveComp):

  def setUp(self):
    self.ctg = CtgType.DATA
    # self.pos = Pos(self.ctg,r=self.r,c=self.c)
    self.label = 'TotallyValidId'
    self.var = 'Stuff?'#ones(self.f_shape)
    self.comp = Locale(label=self.label)

  # @given(st.one_of(st.text(),st.integers(),st.lists(st.integers())))
  # def test_set_var(self, new_var):
  #   if shape in new_var:
  #     self.comp.set_var(new_var[0], new_var[1])
  #     result = self.comp.get_var(new_var[0])
  #     self.assertEqual(result, new_var[1])
  #   else:
  #     with self.assertRaises(RuntimeError):
  #       self.comp.set_var(new_var)

  # def test_get_var(self):
  #   result = self.comp.var
  #   self.assertTrue(array_equal(result, self.var))
  #   self.assertEqual(self.comp.f_shape,self.f_shape)
  #   self.assertEqual(self.comp.s_shape,self.s_shape)
    
if __name__ == '__main__':
  unittest.main()