Feature: Login tests for users
  Tests for logging in users

  @login
  Scenario: Register new user and then log in with the newly created user
    Given User is not logged in.
    And I create a new user.
    Then I go to the login menu I try to login with the newly created user.

  @login
  Scenario: Try and log with Qbet user
    Given User is not logged in.
    And I go to the login menu I try to login with iBet user.
    Then Login was not successful due to non-existing credentials.

  @login
  Scenario: Try and log invalid credentials
    Given User is not logged in.
    And I go to the login menu I try to login with invalid credentials.
    Then User is promted to enter a valid email.

  @login
  Scenario: Register new user and then try to log in with the valid email but invalid password
    Given User is not logged in.
    And I create a new user.
    And I go to the login menu I try to login with the newly created email but invalid password.
    Then Login was not successful due to non-existing credentials.

  @login
  Scenario: Go to register from login menu
    Given User is not logged in.
    And I go to the login menu and I click the register link.
    Then I am taken to the registration menu.