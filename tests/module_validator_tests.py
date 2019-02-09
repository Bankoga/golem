import unittest
from hypothesis import *
from module_validator.py import *
from string import ascii_lowercase
# from config_tests_data.py import *

class ModuleValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = ModuleValidator()

    def test_arbitrary_inputMeldsValidation(self):
        isValid=validator.inputMeldsValidation(inputMelds):
        self.assertTrue(isValid)

    def test_inputMeldsValidation():
        return False

    def test_arbitrary_funcType():
        return False

    def test_funcType():
        return False

    def test_arbitrary_procStageGroupsDict():
        return False

    def test_procStageGroupsDict():
        return False

    def test_arbitrary_procStageShape():
        return False

    def test_procStageShape():
        return False

    def test_arbitrary_procGroupInputMelds():
        return False

    def test_procGroupInputMelds():
        return False

    def test_arbitrary_procGroupDetails():
        return False

    def test_procGroupDetails():
        return False

    def test_arbitrary_procGroupOutputMelds():
        return False

    def test_procGroupOutputMelds():
        return False

    def test_arbitrary_procOutputMelds():
        return False

    def test_procOutputMelds():
        return False

    def test_arbitrary_shapeComposition():
        return False

    def test_shapeComposition():
        return False

    def test_arbitrary_outputMelds():
        return False

    def test_outputMelds():
        return False

    def test_arbitrary_linkMelds():
        return False

    def test_linkMelds():
        return False

    def test_arbitrary_linksDefined():
        return False

    def test_linksDefined():
        return False