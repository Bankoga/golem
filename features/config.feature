@config @initialization
Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # Web scenarios can be highly declarative, which focuses on behavior.
  # Don't get caught up in button names and layouts at the Gherkin level.
  # Note that these scenarios use Selenium WebDriver to do browser interactions.
  # It is popular practice to use imperative steps for service API testing.
  # Karate does this: https://github.com/intuit/karate
  # However, better BDD practice is to use declarative steps.
  # This allows greater code reuse in the automation code.
  # Gherkin-based automation frameworks *can* be used for unit testing.
  # However, they are better suited for integration and end-to-end testing.
  # This feature file does unit testing for the sake of illustrating Gherkin usage.
