import unittest
from hypothesis import *
from module.py import *
from string import ascii_lowercase
# from config_tests_data.py import *

class ModuleTests(unittest.TestCase):
    # TODO: Move the GOLEM conda env from conda envs in AppData local to the package...
    VALID_inputMelds=
    VALID_funcType=
    VALID_procStageGroupsDict=
    VALID_procStageShape=
    VALID_procGroupInputMelds=
    VALID_procGroupDetails=
    VALID_procGroupOutputMelds=
    VALID_procOutputMelds=
    VALID_shapeComposition=
    VALID_outputMelds=
    VALID_linkMelds=
    VALID_linksDefined=
    VALID_funcStrs=[]

    def setUp(self):
        self.module = Module()

    def test_compose_functions(self):
        funcStrs=self.module.compose_functions(
            VALID_inputMelds,
            VALID_funcType,
            VALID_procStageGroupsDict,
            VALID_procStageShape,
            VALID_procGroupInputMelds,
            VALID_procGroupDetails,
            VALID_procGroupOutputMelds,
            VALID_procOutputMelds,
            VALID_shapeComposition,
            VALID_outputMelds,
            VALID_linkMelds,
            VALID_linksDefined)
        self.assertIsNot(funcStrs,NULL)
        self.assertIs(funcStrs,VALID_funcStrs)
    
    def test_arbitrary_compose_functions(self):
        funcStr=self.module.compose_functions(
            funcStr,
            inputMelds,
            funcType,
            procStageGroupsDict,
            procStageShape,
            procGroupInputMelds,
            procGroupDetails,
            procGroupOutputMelds,
            procOutputMelds,
            shapeComposition,
            outputMelds,
            linkMelds,
            linksDefined)
        self.assertIsNot(funcStr,NULL)
        self.assertIs(funcStr,VALID_funcStr)
