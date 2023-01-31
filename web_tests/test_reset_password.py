from pytest_bdd import scenarios, given, then, scenario, when, step
from pytest_bdd.parsers import parse
from web_tests.conftest import userDataGenerator, baseAssertions, adminSteps
from api_resources.api_steps.player_steps import Player
import allure

scenarios('features/forgot_password.feature')


def test_forgot_password():
    print("End of test.")
    pass


@given('I generate new userdata.')
@allure.step("I generate new userdata.")
def generate_new_user_data(context):
    newUserData = userDataGenerator.generateSignupData(countryCode=context.get("country_code"),
                                                       userName=context.get("userName"),
                                                       firstName=context.get("firstName"),
                                                       lastName=context.get("lastName"),
                                                       email=context.get("email"),
                                                       password=context.get("password"),
                                                       phone=context.get("phone"),
                                                       dateOfBirth=context.get("dateOfBirth"),
                                                       street=context.get("street"),
                                                       postCode=context.get("postCode"),
                                                       city=context.get("city"))
    context['user_data'] = newUserData


@given('I create a new user.')
@allure.step("I create a new user.")
def register_new_user(context):
    newRegisteredUserData = Player().registerNewUser()
    context['user_data'] = newRegisteredUserData


@given('User is not logged in.')
@allure.step("User is not logged in.")
def user_not_logged_in(pages):
    pages['about_page'].user_is_not_logged_in()


@then("I should get an error for invalid password.")
@allure.step("I should get an error for invalid password.")
def wrong_creds_error(pages):
    pages["login_page"].wrong_creds_error()


@given("I reset the password.")
@then("I reset the password.")
@allure.step("I reset the password.")
def reset_password(pages, context):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    pages["login_page"].go_to_forgot_password()
    expected_page_title = "Reset password"
    baseAssertions.assertEquals(expected_page_title, pages['forgot_password_page'].get_page_title())
    pages["forgot_password_page"].request_password_reset(context['user_data'])
    context['password'] = pages["forgot_password_page"].set_new_password(context['user_data'])


@given("I go to the reset password page and try to reset the password.")
@allure.step("I go to the reset password page and try to reset the password.")
def reset_password_no_user(pages, context={}):
    context['user_data'] = ""
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    pages["login_page"].go_to_forgot_password()
    expected_page_title = "Reset password"
    baseAssertions.assertEquals(expected_page_title, pages['forgot_password_page'].get_page_title())
    pages["forgot_password_page"].request_password_reset(context['user_data'], invalid=True)


@then("I will receive an not found error.")
@allure.step("I will receive an not found error.")
def get_error(pages):
    pages["forgot_password_page"].check_not_fund_error_is_found()


@then("I reset the password by waiting for the first OTP to expire.")
@allure.step("I reset the password by waiting for the first OTP to expire.")
def reset_password(pages, context):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    pages["login_page"].go_to_forgot_password()
    expected_page_title = "Reset password"
    baseAssertions.assertEquals(expected_page_title, pages['forgot_password_page'].get_page_title())
    pages["forgot_password_page"].request_password_reset(context['user_data'], request_new_OTP=True)
    pages["forgot_password_page"].set_new_password(context['user_data'])


@then("I log in with the new password.")
@allure.step("I log in with the new password.")
def login_with_new_password(pages, context):
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].login_user(context['user_data'], password=context['password'])


@given("I log in with the old password.")
@allure.step("I log in with the old password.")
def login_with_old_password(pages, context):
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].login_user(context['user_data'])


@given("I go to the login menu I try to login with invalid credentials.")
@allure.step("I go to the login menu I try to login with invalid credentials.")
def login_invalid_credentials(pages):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].login_with_invalid_credentials()


@given("I enter a invalid password for password reset.")
@allure.step("I enter a invalid password for password reset.")
def reset_password_invalid(pages, context):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    pages["login_page"].go_to_forgot_password()
    expected_page_title = "Reset password"
    baseAssertions.assertEquals(expected_page_title, pages['forgot_password_page'].get_page_title())
    pages["forgot_password_page"].request_password_reset(context['user_data'])
    context['password'] = pages["forgot_password_page"].set_new_password(context['user_data'], invalid_password=True)


@then("I will get an invalid password error.")
@allure.step("I will get an invalid password error.")
def reset_password(pages):
    pages["forgot_password_page"].check_wrong_pass_err()


