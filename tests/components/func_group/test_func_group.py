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
    self.base_type = self.factory.groups[0].type
    self.group = FuncGroup(self.base_group, self.base_type)
  
  def test_base_properties(self):
    self.assertTrue(self.group.input_rules)
    self.assertTrue(self.group.transform_rules)
    self.assertTrue(self.group.output_rules)

  def test_func(self):
    pass

  def test_build_func(self):
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


