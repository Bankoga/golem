import unittest

from hypothesis import given
from hypothesis import strategies as st


from components.procs.proc_provider import proc_services
from data.axioms.configs import proc_ids, group_types
from components.func_groups.func_group import FuncGroup

class TestFuncGroup(unittest.TestCase):

  def setUp(self):
    self.factory = proc_services.get(proc_ids['glg'])
    self.base_group = self.factory.groups[0]
    self.type = self.factory.groups[0].type
    self.group = FuncGroup(self.base_group, self.type)
  
  def test_address(self):
    # given the rest of the environmental context
    # when I check the address
    # then it should be equal to format(DATA)
    # self.assertTrue(self.group.address)
    pass

  def test_valid_output_packs(self):
    # given the list of proc outputs
    # and the list of link-dest pairing
    # when the output packs are built
    # then there should be N=#links_to+#group_outputs
    # and each pack should contain the correct recipient, sender, resource type, shape
    # self.assertTrue(self.group.output_packs)
    pass

  def test_invalid_output_packs(self):
    # given the list of proc outputs
    # and the list of link-dest pairing
    # when the output packs are built
    # then there should be N=#links_to+#group_outputs
    # and each pack should contain the correct recipient, sender, resource type, shape
    # self.assertTrue(self.group.output_packs)
    pass
  
  def test_resource_types(self):
    # which resource types it accepts from Module level datapacks
    # given the proc group data
    # when the func group is initialized
    # then the accepted_resources list should match resource types
    # self.assertTrue(self.group.resource_types)
    pass
    
  def test_aggrg_func(self):
     # the function used to aggregate the aggregated type inputs
    # takes list of datapacks, and aggregates them according to some rule
    # what would different rules mechanically do?
    # self.assertTrue(self.group.aggrg_func)
    pass

  def test_build_func(self):
    # given a dict of transform labels->output packs [agg|ovrly]->output_pack
    # and a list of transform rules (node rules for proc, and group rules for sensor?)
    # when the function group is completely built
    # each group should have ?????
    pass
    
  def test_transforms_on_valid_input(self):
    # given valid inputs
    # when the transforms are called
    # each result should be ?????
    # dict of labeled sets of input sets (agg,ovrlay) to output packs
    # self.assertTrue(self.group.transforms)
    pass
    
  def test_transforms_on_invalid_input(self):
    # given invalid inputs
    # when the transforms are called
    # WHAT SHOULD HAPPEN?
    pass

  # VALID_inputMelds=
  # VALID_funcType=
  # VALID_procStageGroupsDict=
  # VALID_procStageShape=
  # VALID_procGroupInputMelds=
  # VALID_procGroupDetails=
  # VALID_procGroupOutputMelds=
  # VALID_procOutputMelds=
  # VALID_shapeComposition=
  # VALID_outputMelds=
  # VALID_linkMelds=
  # VALID_linksDefined=
  # VALID_funcStrs=[]

  # def test_compose_functions(self):
  #     funcStrs=self.module.compose_functions(
  #         VALID_inputMelds,
  #         VALID_funcType,
  #         VALID_procStageGroupsDict,
  #         VALID_procStageShape,
  #         VALID_procGroupInputMelds,
  #         VALID_procGroupDetails,
  #         VALID_procGroupOutputMelds,
  #         VALID_procOutputMelds,
  #         VALID_shapeComposition,
  #         VALID_outputMelds,
  #         VALID_linkMelds,
  #         VALID_linksDefined)
  #     self.assertIsNot(funcStrs,NULL)
  #     self.assertIs(funcStrs,VALID_funcStrs)
  
  # def test_arbitrary_compose_functions(self):
  #     funcStr=self.module.compose_functions(
  #         funcStr,
  #         inputMelds,
  #         funcType,
  #         procStageGroupsDict,
  #         procStageShape,
  #         procGroupInputMelds,
  #         procGroupDetails,
  #         procGroupOutputMelds,
  #         procOutputMelds,
  #         shapeComposition,
  #         outputMelds,
  #         linkMelds,
  #         linksDefined)
  #     self.assertIsNot(funcStr,NULL)
  #     self.assertIs(funcStr,VALID_funcStr)


