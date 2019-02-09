@config @initialization @testarchitectures
Feature: Module
  As a cognitive matrix architect,
  I want each module to be internally independent once given the appropriate inputs
  So that the modules can be run effectively in parallel or serial

  Scenario Outline: Build Module Function
    Given the <functionally_valid> <config_name> architecture is prepared
    When a module is initialized
    Then the module function <outcome> <process>

    Examples: Architectures
      | functionally_valid | config_name | outcome | process |
      | True | test-valid | passes | validation |
      | False | test-invalid | fails | initialization |