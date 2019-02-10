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
    VALID_funcStr=

    def setUp(self):
        self.module = Module()

    def test_compose_function(self):
        funcStr=self.module.compose_function(
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
        self.assertIsNot(funcStr,NULL)
        self.assertIs(funcStr,VALID_funcStr)
    
    def test_arbitrary_compose_function(self):
        funcStr=self.module.compose_function(
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
