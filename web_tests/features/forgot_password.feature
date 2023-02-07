Feature: Forgot password tests
  Tests forgotten password

  @password
  Scenario: Register new user and then reset password for user
    Given User is not logged in.
    And I create a new user.
    Then I reset the password.

  @password
  Scenario: Reset password for a email that does not have an account
    Given User is not logged in.
    And I go to the reset password page and try to reset the password.
    Then I will receive an not found error.

  @password
  Scenario: Register new user and then and then reset password for user with an expired OTP code
    Given User is not logged in.
    And I create a new user.
    Then I reset the password by waiting for the first OTP to expire.

  @password
  Scenario: Register new user and then reset password for user then login
    Given User is not logged in.
    And I create a new user.
    And I reset the password.
    Then I log in with the new password.

  @password
  Scenario: Register new user and then reset password for user then login with old password
    Given User is not logged in.
    And I create a new user.
    And I reset the password.
    And I log in with the old password.
    Then I should get an error for invalid password.

  @password
  Scenario: Register new user and then try to reset password with invalid password
    Given User is not logged in.
    And I create a new user.
    And I enter a invalid password for password reset.
    Then I will get an invalid password error.

