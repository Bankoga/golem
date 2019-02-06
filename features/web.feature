@web @duckduckgo
Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # Web scenarios can be highly declarative, which focuses on behavior.
  # Don't get caught up in button names and layouts at the Gherkin level.
  # Note that these scenarios use Selenium WebDriver to do browser interactions.

  Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "panda"
    Then results are shown for "panda"

  Scenario: Lengthy DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for the phrase
      """
      When in the Course of human events, it becomes necessary for one people
       to dissolve the political bands which have connected them with another,
       and to assume among the powers of the earth, the separate and equal
       station to which the Laws of Nature and of Nature's God entitle them,
       a decent respect to the opinions of mankind requires that they should
       declare the causes which impel them to the separation.
      """
    Then one of the results contains "Declaration of Independence"

@service @duckduckgo
Feature: DuckDuckGo Instant Answer API
  As an application developer,
  I want to get instant answers for search terms via a REST API,
  So that my app can get answers anywhere.

  # It is popular practice to use imperative steps for service API testing.
  # Karate does this: https://github.com/intuit/karate
  # However, better BDD practice is to use declarative steps.
  # This allows greater code reuse in the automation code.

  Scenario Outline: Basic DuckDuckGo API Query
    When the DuckDuckGo API is queried with
      | phrase   | format |
      | <phrase> | json   |
    Then the response status code is "200"
    And the response contains results for "<phrase>"

    Examples: Animals
      | phrase   |
      | panda    |
      | python   |
      | platypus |

    Examples: Fruits
      | phrase     |
      | peach      |
      | pineapple  |
      | papaya     |

@unit @basket
Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.

  # Gherkin-based automation frameworks *can* be used for unit testing.
  # However, they are better suited for integration and end-to-end testing.
  # This feature file does unit testing for the sake of illustrating Gherkin usage.

  @add
  Scenario Outline: Add cucumbers to a basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples:
      | initial | some | total |
      | 0       | 3    | 3     |
      | 2       | 4    | 6     |
      | 5       | 5    | 10    |

  @add @full
  Scenario: Fill the basket with cucumbers
    Given the basket is empty
    When "10" cucumbers are added to the basket
    Then the basket is full

  @add @error
  Scenario: Overfill the basket with cucumbers
    Given the basket has "8" cucumbers
    Then "3" cucumbers cannot be added to the basket

  @remove
  Scenario Outline: Remove cucumbers from the basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are removed from the basket
    Then the basket contains "<leftover>" cucumbers

    Examples:
      | initial | some | leftover |
      | 8       | 3    | 5        |
      | 10      | 4    | 6        |
      | 7       | 0    | 7        |

  @remove @empty
  Scenario: Empty the basket of all cucumbers
    Given the basket is full
    When "10" cucumbers are removed from the basket
    Then the basket is empty

  @remove @error
  Scenario: Remove too many cucumbers from the basket
    Given the basket has "1" cucumber
    Then "2" cucumbers cannot be removed from the basket

  @add @remove
  Scenario: Add and remove cucumbers
    Given the basket is empty
    When "4" cucumbers are added to the basket
    And "6" more cucumbers are added to the basket
    But "3" cucumbers are removed from the basket
    Then the basket contains "7" cucumbers
