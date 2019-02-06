import unittest
from hypothesis import *
from config.py import *
from string import ascii_lowercase
# from config_tests_data.py import *

class ConfigTests(unittest.TestCase):
    TODO: Move the GOLEM conda env from conda envs in AppData local to the package...

    def test_module_function_builder(lyrRls, lyrDtls, inMlds, outMlds, gendShpDscrps, lnks):
        return False

    VALID_NAME_CHARS = ascii_lowercase + '_-.'
    
    def valid_module_names():
        return st.text(alphabet=letters, min_size=1, max_size=112).map(lambda t: t.lower()) | st.just("master")

---
Name
LayerRules
LayerDetails
Purpose
Pipeline
InputMelds
Generated Shapes
OutputMelds
Links
Function
Links it defines
Channels
...