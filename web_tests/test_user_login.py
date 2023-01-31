from pytest_bdd import scenarios, given, then, scenario, when, step
from pytest_bdd.parsers import parse
from web_tests.conftest import userDataGenerator, baseAssertions, adminSteps
from api_resources.api_steps.player_steps import Player
import allure

scenarios('features/login.feature')


def test_user_login():
    print("End of test.")
    pass


@then("I go to the login menu I try to login with the newly created user.")
@allure.step("I go to the login menu I try to login with the newly created user.")
def click_register(pages, context):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].login_user(context['user_data'])
    pages["login_page"].check_user_logged_in()


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


@given('the user should exist in the backend.')
@allure.step("the user should exist in the backend.")
def make_admin_api_call_to_fetch_user(context):
    adminSteps.getUsers(userData=context['user_data'])


@then("Login was not successful due to non-existing credentials.")
@allure.step("Login was not successful due to non-existing credentials.")
def wrong_creds_error(pages):
    pages["login_page"].wrong_creds_error()


@then("User is promted to enter a valid email.")
@allure.step("User is promted to enter a valid email.")
def valid_email_error(pages):
    pages["login_page"].valid_email_error()


@given("I go to the login menu I try to login with iBet user.")
@allure.step("I go to the login menu I try to login with iBet user.")
def login_iBet_user(pages):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].login_with_ibet_creds()


@given("I go to the login menu I try to login with invalid credentials.")
@allure.step("I go to the login menu I try to login with invalid credentials.")
def login_invalid_credentials(pages):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].login_with_invalid_credentials()


@given("I go to the login menu I try to login with the newly created email but invalid password.")
@allure.step("I go to the login menu I try to login with the newly created email but invalid password.")
def login_invalid_password(pages, context):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].login_valid_email_invalid_password(context['user_data'])


@given("I go to the login menu and I click the register link.")
@allure.step("I go to the login menu and I click the register link.")
def go_to_registration(pages):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_login_link()
    expected_page_title = "Log in"
    baseAssertions.assertEquals(expected_page_title, pages['login_page'].get_page_title())
    pages["login_page"].go_to_register()


@then("I am taken to the registration menu.")
@allure.step("I am taken to the registration menu.")
def check_registration_menu_present(pages):
    expected_page_title = "Registration"
    baseAssertions.assertEquals(expected_page_title, pages['registration_page'].get_page_title())

