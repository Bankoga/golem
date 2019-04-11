import unittest

from hypothesis import given
from hypothesis import strategies as st

from components.axioms.configs import set_ids
from components.enums.prop_types import SuperSet, GroupType

from components.mediators.module_builder import fs_services
from components.mediators.module import Module

from components.enums.module import ModuleType
from components.enums.pos import CtgType
from components.matrix.lineage_registry import LineageRegistry
from components.matrix.channel_registry import ChannelRegistry
from components.vars.data import Lineage
from tests.strategies.module_strats import module_input_set
from tests.components.base.test_plastic_comp import TestPlasticComp
from tests.components.base.mechanisms.mediators.test_mediator import TestMediator

class TestModule(TestMediator,TestPlasticComp):
  def set_up_base(self):
    self.label = 'TotallyValidId'
    self.ctg = CtgType.MODULE
    self.comp_class = Module

  def set_up_layers(self):
    self.layers = 0

  def set_up_var(self):
    self.registry = LineageRegistry(label='global_lineage_registry_api')
    self.channel_registry = ChannelRegistry(label='global_channel_registry_api')
    self.lineage_registry = self.registry
    self.lineage = Lineage(golem='a',matrix='l',module='glg')
    self.reg_item = {
      'reg_id': self.label,
      'lineage': self.lineage
    }
    self.module_type = ModuleType.GLG
    self.set_up_layers()
    self.b2 = 0
    self.b3 = 0
    self.values = [self.registry, self.channel_registry, self.module_type]
    self.var = tuple(self.values)
    self.baseline = self.values

  def setUp(self):
    self.set_up_base()
    self.set_up_defaults()
    # self.id = proc_ids['glg']
    # self.factory = proc_services.get(self.id)
    # self.base_group = self.factory.groups[0]
    # self.ctg_type = self.factory.groups[0].ctg_type
    # self.fg = Module(self.id, self.ctg_type)
    self.set_up_var()
    self.comp = self.comp_class(*self.values,label=self.label)
    # self.fs_id = set_ids['glg']
    # self.module_type = SuperSet.PROC
    # self.fset = fs_services.get(f'{self.module_type}-{self.fs_id}')
    # self.fset.build()
  
  # def test_get_b2(self):
  #   self.assertEqual(self.comp.b2, self.b2)
  # def test_set_b2(self):
  #   with self.assertRaises(RuntimeError):
  #     self.comp.b2 = self.b2

  # def test_get_b3(self):
  #   self.assertEqual(self.comp.b3, self.b3)
  # def test_set_b3(self):
  #   with self.assertRaises(RuntimeError):
  #     self.comp.b3 = self.b3

  # def test_get_layers(self):
  #   self.assertEqual(self.comp.layers, self.layers)
  # def test_set_layers(self):
  #   with self.assertRaises(RuntimeError):
  #     self.comp.layers = self.layers

  def test_get_module_type(self):
    self.assertEqual(self.comp.module_type, self.module_type)
  def test_set_module_type(self):
    with self.assertRaises(RuntimeError):
      self.comp.module_type = self.module_type

  def test_build_group(self):
    pass
  
  def test_build_groups(self):
    pass
  
  def test_build_layer(self):
    pass
  
  def test_build_layers(self):
    pass
  
  def test_build_(self):
    pass

  # def test_?(self):
  #   with self.assertRaises(NotImplementedError):
  #     self.fset.?()
  # def test_build_funcs(self):
  #   alt_fset = fs_services.get(f'{self.module_type}-{self.fs_id}')
  #   base_groups = alt_fset.groups
  #   for set_id in base_groups:
  #     g_dat = base_groups[set_id]
  #     g_type = GroupType[g_dat['group_type']]
  #     expectation = Module(g_dat,g_type)
  #     result = self.fset.groups[set_id]
  #     self.assertEqual(result, expectation)
  

  # def test_operate(self):
  #   pass
  # # # TODO: Move the GOLEM conda env from conda envs in AppData local to the package...
  # @given(module_input_set(st.just('TestC'))) # pylint: disable=no-value-for-parameter
  # def test_process(self, inputs):
  #   pass

  # def test_get_component_type(self):
  #   pass

  # def test_lineage(self):
  #   # given the rest of the environmental context
  #   # when I check the lineage
  #   # then it should be equal to format(DATA)
  #   # self.assertTrue(self.group.lineage)
  #   pass

  # def test_valid_output_packs(self):
  #   # given the list of proc outputs
  #   # and the list of link-dest pairing
  #   # when the output packs are built
  #   # then there should be N=#links_to+#group_outputs
  #   # and each pack should contain the correct recipient, sender, resource type, shape
  #   # self.assertTrue(self.group.output_packs)
  #   pass

  # def test_invalid_output_packs(self):
  #   # given the list of proc outputs
  #   # and the list of link-dest pairing
  #   # when the output packs are built
  #   # then there should be N=#links_to+#group_outputs
  #   # and each pack should contain the correct recipient, sender, resource type, shape
  #   # self.assertTrue(self.group.output_packs)
  #   pass
  
  # def test_resource_types(self):
  #   # which resource types it accepts from Module level packages
  #   # given the proc group data
  #   # when the func set is initialized
  #   # then the accepted_resources list should match resource types
  #   # self.assertTrue(self.group.resource_types)
  #   pass
    
  # def test_aggrg_func(self):
  #    # the function used to aggregate the aggregated type inputs
  #   # takes list of packages, and aggregates them according to some rule
  #   # what would different rules mechanically do?
  #   # self.assertTrue(self.group.aggrg_func)
  #   pass

  # def test_build_func(self):
  #   # given a dict of transform labels->output packs [agg|ovrly]->output_pack
  #   # and a list of transform rules (node rules for proc, and group rules for sensor?)
  #   # when the function group is completely built
  #   # each group should have ?????
  #   pass
    
  # def test_transforms_on_valid_input(self):
  #   # given valid inputs
  #   # when the transforms are called
  #   # each result should be ?????
  #   # dict of labeled sets of input sets (agg,ovrlay) to output packs
  #   # self.assertTrue(self.group.transforms)
  #   pass
    
  # def test_transforms_on_invalid_input(self):
  #   # given invalid inputs
  #   # when the transforms are called
  #   # WHAT SHOULD HAPPEN?
  #   pass

  # # VALID_inputMelds=
  # # VALID_funcType=
  # # VALID_procStageGroupsDict=
  # # VALID_procStageShape=
  # # VALID_procGroupInputMelds=
  # # VALID_procGroupDetails=
  # # VALID_procGroupOutputMelds=
  # # VALID_procOutputMelds=
  # # VALID_shapeComposition=
  # # VALID_outputMelds=
  # # VALID_linkMelds=
  # # VALID_linksDefined=
  # # VALID_funcStrs=[]

  # # def test_compose_functions(self):
  # #     funcStrs=self.module.compose_functions(
  # #         VALID_inputMelds,
  # #         VALID_funcType,
  # #         VALID_procStageGroupsDict,
  # #         VALID_procStageShape,
  # #         VALID_procGroupInputMelds,
  # #         VALID_procGroupDetails,
  # #         VALID_procGroupOutputMelds,
  # #         VALID_procOutputMelds,
  # #         VALID_shapeComposition,
  # #         VALID_outputMelds,
  # #         VALID_linkMelds,
  # #         VALID_linksDefined)
  # #     self.assertIsNot(funcStrs,NULL)
  # #     self.assertIs(funcStrs,VALID_funcStrs)
  
  # # def test_arbitrary_compose_functions(self):
  # #     funcStr=self.module.compose_functions(
  # #         funcStr,
  # #         inputMelds,
  # #         funcType,
  # #         procStageGroupsDict,
  # #         procStageShape,
  # #         procGroupInputMelds,
  # #         procGroupDetails,
  # #         procGroupOutputMelds,
  # #         procOutputMelds,
  # #         shapeComposition,
  # #         outputMelds,
  # #         linkMelds,
  # #         linksDefined)
  # #     self.assertIsNot(funcStr,NULL)
  # #     self.assertIs(funcStr,VALID_funcStr)

  # @given(module_input_set(st.just(set_ids['glg']))) # pylint: disable=no-value-for-parameter
  # def test_process_inputs(self):
  #   # in the beginning, we have a list of unordered, and unaggregated inputs
  #   pass
  # def test_operate(self):
  #   pass
  # # # TODO: Move the GOLEM conda env from conda envs in AppData local to the package...
  # @given(module_input_set(st.just('TestC'))) # pylint: disable=no-value-for-parameter
  # def test_process(self, inputs):
  #   pass
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



if __name__ == '__main__':
  unittest.main()