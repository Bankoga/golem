import utils.object_factory
from components.func_groups.fg_builder_provider import fg_services
import unittest
from hypothesis import given
from hypothesis import strategies as st
from  data.axioms.enums import FuncGroup

class TestFGBuilderProvider(unittest.TestCase):
  @given(st.sampled_from(sorted(FuncGroup)))
  def test_get(self, fg_type_id):
    ordinator = fg_services.get(fg_type_id, **{})
    self.assertTrue(ordinator.get_id(), fg_type_id)
    
if __name__ == '__main__':
    unittest.main()