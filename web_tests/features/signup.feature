Feature: Register new users tests
  Tests for registering new users functionality

  @signup
  Scenario Outline: Register new user with different countries
    Given There is the following country we want to test with <countryCode>.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form.
    And I fill in the second registration form.
    And I enter the sms code.
    Then the user should exist in the backend.

    Examples:
    | countryCode |
    | Sweden      |
    | Finland     |
    | Norway      |

  @signup
  Scenario Outline: Register new user with accepting Terms and Conditions and Personal Data Handling
    Given There is the following sign-up agreement combination we want to test with <agreements>.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form.
    And I fill in the second registration form.
    And I enter the sms code.
    Then the user should exist in the backend.

    Examples:
    | agreements                      |
    | termsAndConditions cookiePolicy |
    | agreeAll                        |

  @signup
  Scenario Outline: Register new user without accepting Terms and Conditions and Personal Data Handling
    Given There is the following sign-up agreement combination we want to test with <agreements>.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form.
    And I fill in the second registration form.
    Then The continue button will be greyed out due to not accepting the correct agreements.

    Examples:
    | agreements           |
    | cookiePolicy         |
    | offers               |
    | offers cookiePolicy  |

  @signup
  Scenario: Register new user with missing or invalid information
    Given User is not logged in.
    And I generate new userdata.
    When I go to the registration menu.
    And I fill in the first registration form with invalid data.
    And I fill in the second registration form with invalid data.
    And I enter the sms code.
    Then the user should exist in the backend.

