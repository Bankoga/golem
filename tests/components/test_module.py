import unittest

from hypothesis import given
from hypothesis import strategies as st

# from data.tests.dummy_configs import module_all_groups

from components.func_groups.fg_builder_provider import fg_services
from components.module import Module

from data.axioms.configs import group_ids

from tests.strategies.golem_strats import module_input_set

class TestModule(unittest.TestCase):
  def setUp(self):
    fg_id = group_ids['glg']
    fg_type = GroupType.SENSOR
    group = fg_service.get(f'{fg_type}-{fg_id}'')
    self.module = Module(group)
    # self.module = Module(module_all_groups)

  def test_build_function_groups(self):
    pass

  def test_operate(self):
    pass
  # # TODO: Move the GOLEM conda env from conda envs in AppData local to the package...
  
  @given(module_input_set(st.just('TestC'))) # pylint: disable=no-value-for-parameter
  def test_process(self, inputs):
    pass

if __name__ == '__main__':
    unittest.main()


  # def test_hooks_were_inserted_correctly(self):
  #   hook_prop = 'hooks'
  #   if hook_prop in self.proc_conf:
  #     hooks = self.proc_conf[hook_prop]
  #     if hooks is None:
  #       for group in self.proc.groups:
  #         self.assertIsNone(group[hook_prop])
  #     else:
  #       for i,hook_id in hooks:
  #         self._check_hook_group_(hook_id,hooks[i])
  
  # def _check_hook_group_(self,hook_id,hook_group):
  #   # if hook_group['direction'] == 'to':
  #   #   self.assertIn(
  #   #     hook,
  #   #     self.proc.groups[hook_group]['outputs']
  #   #   )
  #   TODO: Specify behavior of the hook types that get added to a groups outputs
  #   if hook_group['direction'] == 'from':
  #     for targ in hook_group['targets']:
  #     self.assertIn(
  #       ';'.split(targ)[2:],
  #       self.proc.groups[hook_group]['outputs']
  #     )
  #   # else:
  #     # self.assertRaises()
  
  # #  TODO: READ HOOK DEFINITIONS METHOD CHECK. Its not going to be done during init though
  # # hook definitions will be called during golem building in order to finish off hook packages
  # # i don't think it will be needed before then though
