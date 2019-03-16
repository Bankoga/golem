import unittest

from hypothesis import given
from hypothesis import strategies as st
from numpy import array_equal, ones

from components.data.conv_shape import ConvShape
from components.enums.pos import CtgType
from components.vars.data import ConvVar
from tests.components.base.test_passive_comp import TestPassiveComp
from tests.strategies.data_strats import valid_resource_data
from utils.pos import Pos


class TestConvShape(TestPassiveComp):

  def setUp(self):
    self.filter_shape = (4,4)
    self.spacing_shape = (1,1)
    self.source_id = 'ID_of_locale_used_for_source_index'
    self.source_index = (5,5)
    self.weights = ones(self.filter_shape)
    self.var = ConvVar(source_id=self.source_id,
     source_index=self.source_index,
     filter_shape=self.filter_shape,
     spacing_shape=self.spacing_shape,
    weights=self.weights)
    self.ctg = CtgType.DATA
    self.label = 'TotallyValidId'
    self.comp = ConvShape(self.source_id,self.source_index, self.filter_shape, self.spacing_shape,label=self.label)

  def test_get_var(self):
    self.assertTrue(self.comp.var, self.var)

  def test_get_weights(self):
    self.assertTrue(array_equal(self.comp.weights, self.weights))

  def test_get_filter_shape(self):
    self.assertEqual(self.comp.filter_shape, self.filter_shape)

  def test_get_spacing_shape(self):
    self.assertEqual(self.comp.spacing_shape, self.spacing_shape)
  
  def test_get_source_index(self):
    self.assertEqual(self.comp.source_index, self.source_index)

  def test_get_source_id(self):
    self.assertEqual(self.comp.source_id, self.source_id)

  def test_set_weights(self):
    with self.assertRaises(RuntimeError):
      self.comp.weights = 'Does not matter'

  def test_set_filter_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.filter_shape = 'Does not matter'

  def test_set_spacing_shape(self):
    with self.assertRaises(RuntimeError):
      self.comp.spacing_shape = 'Does not matter'
  
  def test_set_source_index(self):
    with self.assertRaises(RuntimeError):
      self.comp.source_index = 'Does not matter'

if __name__ == '__main__':
  unittest.main()
