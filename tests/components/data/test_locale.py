# import unittest

# from hypothesis import given
# from hypothesis import strategies as st

# from tests.components.base.test_passive_comp import TestPassiveComp
# from tests.strategies.data_strats import valid_locale_inputs

# from components.data.locale import Locale
# from components.enums.pos import CtgType
# from components.vars.data import locale

# from utils.pos import Pos

# class TestLocale(TestPassiveComp):

#   def setUp(self):
#     self.ctg = CtgType.DATA
#     self.lineage = 'm_0'
#     self.pos = Pos(self.ctg)
#     self.label = 'TotallyValidId'
#     self.var = (self.lineage,self.pos)
#     self.comp = Locale(self.lineage, self.pos, label=self.label)

#   @given(valid_locale_inputs()) # pylint: disable=no-value-for-parameter
#   def test_set_var(self, new_var):
#     if not new_var is None:
#       with self.assertRaises(RuntimeError):
#         self.comp.var = new_var
#     else:
#       self.comp.var = new_var

#   def test_get_var(self):
#     self.assertEqual(self.comp.var, self.var)

#   def test_get_lineage(self):
#     self.assertEqual(self.comp.lineage, self.lineage)
  
#   def test_get_pos(self):
#     self.assertEqual(self.comp.pos, self.pos)
  
#   # def test_set_invalid_lineage(self, lineage):
#   #   pass

#   # def test_set_lineage(self, lineage):
#   #   pass

#   # def test_set_invalid_pos(self, lineage):
#   #   pass

#   # def test_set_pos(self, lineage):
#   #   pass

#   # def test_update_lineage(self,new_lineage):
#   #   pass
    
#   # def test_update_pos(self,new_pos):
#   #   pass
    


#   # @given(valid_locale()) # pylint: disable=no-value-for-parameter
#   # def test_get_pos_in(self, locale):
#   #   pass

#   # def test_locale(self):
#   #   pass
#   # @given(st.one_of(st.text(),st.integers(),st.lists(st.integers())))
#   # def test_set_var(self, new_var):
#   #   if shape in new_var:
#   #     self.comp.set_var(new_var[0], new_var[1])
#   #     result = self.comp.get_var(new_var[0])
#   #     self.assertEqual(result, new_var[1])
#   #   else:
#   #     with self.assertRaises(RuntimeError):
#   #       self.comp.set_var(new_var)

#   # def test_get_var(self):
#   #   result = self.comp.var
#   #   self.assertTrue(array_equal(result, self.var))
#   #   self.assertEqual(self.comp.f_shape,self.f_shape)
#   #   self.assertEqual(self.comp.s_shape,self.s_shape)
    
# if __name__ == '__main__':
#   unittest.main()