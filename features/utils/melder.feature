@initialization @melds
Feature: Melder
  As a golem,
  I want each meld to have the same sets of properties
  So that they can be used to dynamically generate lists of shapes dictionaries

  Scenario Outline: Eval Meld
    Given a <meld> string of <type>
    When it is evaluated
    Then <count> results should be in the <format>

    Examples: SingleResourcePatterns
    | meld | type | count | format |
    | ?,Resource | InputMeld | ? | ?|
    | ?,Resource | ProcGroupInputMeld | ? | ?|
    | ?,Resource | ProcGroupOutputMeld | ? | ?|
    | ?,Resource | OutputMeld | ? | ?|
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

  Scenario Outline: Eval Melds
    Given a list of meld <templates>
    And WHAT DATA IS REQ?
    When the full list of melds is evaluated
    Then <count> results should be in the <format>

    Examples: InputMelds
      | templates | ? | count | format |
      | ? | ? | ? | ? |
      | ? | ? | ? | ? |

    Examples: ProcGroupInputMelds
      | templates | ? | count | format |
      | ? | ? | ? | ? |
      | ? | ? | ? | ? |

    Examples: ProcGroupOutputMelds
      | templates | ? | count | format |
      | ? | ? | ? | ? |
      | ? | ? | ? | ? |

    Examples: OutputMelds
      | templates | ? | count | format |
      | ? | ? | ? | ? |
      | ? | ? | ? | ? |

    Examples: LinkMelds
      | templates | ? | count | format |
      | ? | ? | ? | ? |
      | ? | ? | ? | ? |