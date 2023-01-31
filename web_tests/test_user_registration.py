from pytest_bdd import scenarios, given, then, scenario, when, step
from pytest_bdd.parsers import parse
from web_tests.conftest import userDataGenerator, baseAssertions, adminSteps
import allure

scenarios('features/signup.feature')


def test_user_registration():
    print("End of test.")
    pass


@given(parse('There is the following country we want to test with {countryCode}.'),
       converters=dict(countryCode=str))
@allure.step("There is the following country we want to test with {countryCode}.")
def country_codes(countryCode, context):
    context['country_code'] = countryCode


@given(parse('There is the following sign-up agreement combination we want to test with {agreements}.'),
       converters=dict(agreement=str))
@allure.step("There is the following sign-up agreement combination we want to test with {agreements}.")
def country_codes(agreements, context):
    context['agreements'] = agreements


@when("I go to the registration menu.")
@allure.step("I go to the registration menu")
def click_register(pages):
    pages["about_page"].click_cookie_pop_up_ok_btn()
    pages["about_page"].click_register_link()
    expected_page_title = "Registration"
    baseAssertions.assertEquals(expected_page_title, pages['registration_page'].get_page_title())


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


@given('User is not logged in.')
@allure.step("User is not logged in.")
def user_not_logged_in(pages):
    pages['about_page'].user_is_not_logged_in()


@when('I fill in the first registration form.')
@allure.step("I fill in the first registration form.")
def registration_table_1(pages, context, browser):
    newUserData = context['user_data']
    pages['registration_page'].register_step_1(newUserData, browser=browser)


@when('I fill in the first registration form with invalid data.')
@allure.step("I fill in the first registration form with missing and invalid data.")
def registration_table_1_invalid_check(pages, context, browser):
    newUserData = context['user_data']
    pages['registration_page'].register_step_1_invalid_data()
    pages['registration_page'].register_step_1(newUserData, browser=browser)


@when('I fill in the second registration form with invalid data.')
@allure.step("I fill in the second registration form with missing and invalid data.")
def registration_table_2_invalid_check(pages, context):
    newUserData = context['user_data']
    pages['registration_page'].register_step_2_invalid_data()
    pages['registration_page'].register_step_2(newUserData)


@when('I fill in the second registration form.')
@allure.step("I fill in the second registration form.")
def registration_table_2(pages, context):
    newUserData = context['user_data']
    pages['registration_page'].register_step_2(newUserData, context.get("agreements"))


@when(parse('I fill in the deposit and play registration with {amount}.'),
      converters=dict(amount=str))
@allure.step("I fill in the deposit and play registration with {amount}.")
def register_deposit_pay_and_play(pages, context, amount):
    newUserData = context['user_data']
    pages['registration_page'].register_with_deposit_and_play(newUserData, amount)


@when('I enter the sms code.')
@allure.step("I enter the sms code.")
def registration_table_3(pages):
    pages['registration_page'].register_step_3()


@then('the user should exist in the backend.')
@allure.step("the user should exist in the backend.")
def make_admin_api_call_to_fetch_user(context):
    adminSteps.getUsers(userData=context['user_data'])


@then('The continue button will be greyed out due to not accepting the correct agreements.')
@allure.step("The continue button will be greyed out due to not accepting the correct agreements.")
def check_continue_button_status(pages):
    baseAssertions.assertEquals(False, pages["registration_page"].is_continue_button_enabled())
