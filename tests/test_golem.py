import unittest
from yaml import load, dump
import unittest
from hypothesis import given
import hypothesis.strategies as st

# from components.axioms.props import dest_key_pattern 
# from utils.config_reader import read
from golem import Golem

class TestGolem(unittest.TestCase):
  def set_up_base(self):
    pass
    
  def set_up_defaults(self):
    pass
  
  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    self.golem = Golem()

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