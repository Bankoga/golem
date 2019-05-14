import unittest
from yaml import load, dump
import unittest
from hypothesis import given
import hypothesis.strategies as st

# from components.axioms.props import dest_key_pattern 
# from utils.config_reader import read
from golem import Golem
from utils.helpers.namerinator import roll_name
from tests.strategies.prop_strats import arb_name

class TestGolem(unittest.TestCase):
  def set_up_base(self):
    self.name = roll_name()
    
  def set_up_defaults(self):
    pass
  
  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.golem = Golem(self.name)

  def test_get_name(self):
    self.assertTrue(self.golem.name, self.name)

  @given(arb_name()) # pylint: disable=no-value-for-parameter
  def test_set_name(self, name):
    self.golem.name = name
    self.assertEqual(self.golem.name, name)

  def test_init(self):
    pass

  def test_get_config(self):
    self.assertTrue(self.golem.config)

  def test_set_config(self):
    with self.assertRaises(RuntimeError):
      self.golem.config = 'anything'
  
  def test_load_config(self):
    pass
  
  def test_read_config(self):
    pass

  def test_create(self):
    pass

  def test_run(self):
    pass

  def test_chat_interface(self):
    pass

if __name__ == '__main__':
    unittest.main()