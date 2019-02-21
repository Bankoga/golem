import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.hooks.hook import Hook

class TestHook(unittest.TestCase):
  # def setUp(self):
    # self.hook = Hook()

  @given(st.text(), st.text(), st.text())
  def test_init(self, hook_id, direction, target):
    hook = Hook(hook_id, direction, target)
    self.assertEqual(hook.id, hook_id)
    self.assertEqual(hook.direction, direction)
    self.assertEqual(hook.target, target)