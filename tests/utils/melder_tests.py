import unittest
from hypothesis import given
import hypothesis.strategies as st
from utils.melder import *
from utils.datapack import *
from string import ascii_lowercase
from data.axioms.matrix import resource_types
from data.axioms.matrix import dest_key_pattern
# from config_tests_data.py import *

# It is an open question as to whether or not links need to be defined as part of the proc group

class MelderTests(unittest.TestCase):
  def setUp(self):
    self.melder = Melder()

  # def test_eval_melds(self, meld):
  #   """given a list of meld templates, and WHAT DATA IS REQ?
  #   When the full list of melds is evaluated
  #   Then <count> results should be in the <format>"""
  #   self.assertTrue(False)

  # FOR EACH SET OF MELDTYPES/PATTERNS/FORMATS THAT ARE HANDLED IN THEIR OWN FUNCTION HAVE UNIQUE TEST METHOD
  @given(st.from_regex(f'{dest_key_pattern},({"|".join(resource_types.keys())})(,SHAPE)'))
  def test_eval_full_meld(self, meld):
    datp = self.melder.eval_meld(meld)
    self.assertIsInstance(datp,Datapack)
    parts=meld.split(",")
    self.assertTrue(datp.address==parts[0])
    self.assertTrue(datp.resource==parts[1])
    self.assertTrue(datp.shape==parts[2])

  @given(st.from_regex(f'{dest_key_pattern},({"|".join(resource_types.keys())})'))
  def test_eval_proto_meld(self, meld):
    datp = self.melder.eval_meld(meld)
    self.assertIsInstance(datp,Datapack)
    parts=meld.split(",")
    self.assertTrue(datp.address!=parts[0])
    self.assertTrue(datp.resource!=parts[1])

  @given(st.from_regex(f'{dest_key_pattern},({"|".join(resource_types.keys())})(,SHAPE)'))
  def test_eval_proto_melds(self, meld):
    datp = self.melder.eval_meld(meld)
    self.assertIsInstance(datp,list(Datapack))
    parts=meld.split(",")
    self.assertTrue(datp.address==parts[0])
    self.assertTrue(datp.resource==parts[1])
    self.assertTrue(datp.shape==parts[2])

"""
4/5 Sources of Melds from a Module Config
  InputMeld
  ProcGroupInputMeld
  ProcGroupOutputMeld
  OutputMeld
  LinkMeldRules(AllLinkDefinitions + Links + LocalLinkDefinitions)
I/O Melds have the same property format
ProcGroup I/O Melds have the same property format
Link related melds show up in all 4 of the other Sources
LinkMelds is curr only being used for outputs to links, and links a thing is part of
Both property formats use the same meld formats

LinkId + '_i' indicates that each link is a new instance (to the extent that it is basically pseudo-module)


It seems like each type of pattern, is its own test case
Scenario Outline: Eval Meld
  Given a <meld> string of <type>
  When it is evaluated
  Then <count> results should be in the <format>

  Examples: SingleResourcePatterns
  | meld | type | count | format |




  | [],Resource | ? | ? | ?|
  | [ID],Resource | LinkMeld | ? | ?|
  | ID,Resource | LinkMeld | ? | ?|
  | ID_?,Resource | LinkMeld | ? | ?|
  | [ID_?],Resource | LinkMeld | ? | ?|

  Examples: MultiResourcePatterns
  | meld | type | count | format |
  | A,[ResourceA,ResourceB] | ? | ? | ?|
  | A,[ResourceA,ResourceB],SHAPE | ? | ? | ?|
  | ?,[ResourceA,ResourceB],SHAPE | ? | ? | ?|
  | [],[ResourceA,ResourceB] | ? | ? | ?|
  | [ID],[ResourceA,ResourceB] | LinkMeld | ? | ?|
  | ID,[ResourceA,ResourceB] | LinkMeld | ? | ?|
  | ID_?,[ResourceA,ResourceB] | LinkMeld | ? | ?|
  | [ID_?],[ResourceA,ResourceB] | LinkMeld | ? | ?|


Every data bearing connection between two components (modules, nodes, or otherwise) is a Meld.
All melds have the same overall full format, with several definitional formats.
A melder object can be used to do the following:
- convert descriptions of melds, into lists of proto-melds
- convert a destination pattern into a a list of proto-melds
- convert a list of proto-melds into full melds

- Full: Module_key-subdest,Resource_type,Field_shape
- Definition_A: Link_key,Resource_types

Each link type can have it's own field shape that needs to be accounted for, and each link must be counted separately so we have to dynamically generate all link input and output melds anywhere a link id is specified

"""