import logging

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.top_bars.top_menu_bar import TopMenuBar
import time
from helper_enums.help_enums import Enums, ValueEnums
from api_core.microservices.apibase.assertions.userAssertions import BaseAssertions

baseAssertions = BaseAssertions()


class RegistrationPage(TopMenuBar):
    """ Login Page """
    PAGE_TITLE = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[1]/div[1]/div[1]")
    FIRST_NAME = (By.XPATH, "//*[@id=\"firstName\"]")

    LAST_NAME = (By.XPATH, "//*[@id=\"lastName\"]")
    PASSWORD = (By.XPATH, "//*[@id=\"password\"]")
    EMAIL = (By.XPATH, "//*[@id=\"email\"]")
    PHONE = (By.XPATH, "//*[@id=\"phoneBody\"]")
    COUNTRYCODE_DROPDOWN = (By.XPATH, "//*[@id=\"phonePrefix\"]")
    DATEOFBIRTH = (By.XPATH, "//*[@id=\"dateOfBirth\"]")
    STREET = (By.XPATH, "//*[@id=\"street\"]")
    CITY = (By.XPATH, "//*[@id=\"city\"]")
    POSTCODE = (By.XPATH, "//*[@id=\"postCode\"]")
    GENDER = (By.XPATH, "// *[ @ id = \"gender\"] / label[1] / span[1]")
    AGREE_ALL = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[8]/fieldset/label/span[1]")
    SMS_CODE = (By.XPATH, "//*[@id=\"pincode-0\"]")
    AGREE_TERMS = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[8]/fieldset/div[1]/label/span["
                             "1]/span[1]")
    AGREE_COOKIE = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[8]/fieldset/div["
                              "2]/label/span[1]/span[1]")
    AGREE_OFFERS = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[8]/fieldset/div["
                              "3]/label/span[1]/span[1]")

    CONTINUE_BTN_STEP_1 = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/button")
    CONTINUE_BTN_STEP_2 = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/button")
    VERIFY_SMS_BTN = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/div[1]/button/span")

    EMAIL_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[3]/div/p")
    PASSWORD_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[4]/div/p")
    LAST_NAME_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[1]/div/p")
    FIRST_NAME_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[1]/div/p")
    STREET_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[5]/div/p")
    CITY_WARNING = (By.XPATH, "// *[ @ id = \"signupModal\"] / div / div[2] / section / form / div / div[6] / div / p")
    POSTCODE_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[6]/div/p")
    BIRTHDATE_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[3]/div/p")

    REGISTER_DEPOSIT_AND_PLAY = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[1]/div[1]/div[2]")
    PAY_AND_PLAY_AMOUNT = (By.XPATH, "//*[@id=\"amount\"]")
    START_PLAYING = (By.XPATH, "// *[ @ id = \"signupModal\"] / div / div[2] / div / section / div[2] / button")

    BANKS_IFRAME = (By.XPATH, "//*[@id=\"deposit\"]")
    NORDEA_BANK = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div/ul/div[1]/div/div[2]")

    JATKA_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[2]/div/button")
    LAST_JAKTA_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]/button")
    CONTINUE_PNP = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[2]/div/button")
    LOGIN_ID = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[1]/div/div/div")
    ONE_TIME_CODE = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[1]/div[1]/div/div/h3")
    ONE_TIME_CODE_BOX = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[1]/div[2]/div/div/input")

    CHECKING_ACCOUNT = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div/div[2]/div/ul/div[1]/div/div[1]/div/div["
                                  "1]/span[1]")
    EMAIL_PAY_N_PLAY = (By.XPATH, "//*[@id=\"emailPayNPlay\"]")
    PASSWORD_PAY_N_PLAY = (By.XPATH, "//*[@id=\"passwordPayNPlay\"]")
    PHONE_PAY_N_PLAY = (By.XPATH, "//*[@id=\"phoneBodyPayNPlay\"]")
    AGREE_ALL_PAY_N_PLAY = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/div/section/form/div/div[5]/fieldset/label")

    REGISTER_PAY_N_PLAY = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/div/section/div[2]/button")

    COUNTRYCODE_DICT = {'Egypt': 43, 'El Salvador': 40, 'Mexico': 78, 'Sweden': 115, 'Finland': 44, 'Norway': 95}

    def __init__(self, driver):

        super().__init__(driver)

    logger = logging.getLogger(__name__)

    @allure.step("Register to website with required data from the new user data dictionary - step 1.")
    def register_step_1(self, newUserData, browser):

        """Initialise the variables that need for this step."""
        firstName = newUserData.firstName
        lastName = newUserData.lastName
        email = newUserData.email
        password = newUserData.password
        phone = newUserData.phone
        countryCode = newUserData.countryCode

        self.fill_text(self.FIRST_NAME, firstName)
        self.fill_text(self.LAST_NAME, lastName)
        self.fill_text(self.EMAIL, email)
        self.fill_text(self.PASSWORD, password)
        self.scroll_down()

        if countryCode is not None:
            self.click(self.COUNTRYCODE_DROPDOWN)
            COUNTRY_CODE = self.get_country(countryCode)
            self.get_element(COUNTRY_CODE)
            self.click(COUNTRY_CODE)

        self.fill_text(self.PHONE, phone)

        if browser == Enums.MOBILE.value:
            self.select_for_mobile()
        else:
            if self.is_elem_enabled(self.CONTINUE_BTN_STEP_1):
                self.click(self.CONTINUE_BTN_STEP_1)

    @allure.step("Register to website and verify that missing or incorrect fields have warnings - step 1.")
    def register_step_1_invalid_data(self):

        self.fill_text(self.FIRST_NAME, ValueEnums.BOGUS_VALUE.value)
        self.delete_with_keys(self.FIRST_NAME, len(str(ValueEnums.BOGUS_VALUE.value)))
        self.fill_text(self.LAST_NAME, ValueEnums.BOGUS_VALUE.value)
        self.delete_with_keys(self.LAST_NAME, len(str(ValueEnums.BOGUS_VALUE.value)))
        self.fill_text(self.EMAIL, ValueEnums.BOGUS_VALUE.value)
        self.delete_with_keys(self.EMAIL, len(str(ValueEnums.BOGUS_VALUE.value)))
        self.fill_text(self.PASSWORD, ValueEnums.BOGUS_VALUE.value)
        self.delete_with_keys(self.PASSWORD, len(str(ValueEnums.BOGUS_VALUE.value)))
        self.click(self.PHONE)
        self.scroll_down()

        self.is_warning_visible(self.EMAIL_WARNING)
        self.is_warning_visible(self.FIRST_NAME)
        self.is_warning_visible(self.LAST_NAME)
        self.is_warning_visible(self.EMAIL_WARNING)
        self.is_warning_visible(self.PASSWORD_WARNING)

        status = self.is_elem_enabled(self.CONTINUE_BTN_STEP_1)
        baseAssertions.assertEquals(False, status)

    @allure.step("Register to website with required data from the new user data dictionary - step 2.")
    def register_step_2(self, newUserData, agreements=None):

        """Initialise the variables that need for this step."""
        dateOfBirth = newUserData.dateOfBirth
        postCode = newUserData.postCode
        city = newUserData.city
        street = newUserData.street

        self.click(self.DATEOFBIRTH)
        self.fill_text(self.DATEOFBIRTH, dateOfBirth)
        self.click(self.GENDER)
        self.fill_text(self.STREET, street)
        self.fill_text(self.CITY, city)
        self.fill_text(self.POSTCODE, postCode)
        self.scroll_down()
        if agreements is None:
            self.click(self.AGREE_ALL)
        else:
            self.click_agreements(agreements)

        self.scroll_down()
        if self.is_elem_enabled(self.CONTINUE_BTN_STEP_2):
            self.click(self.CONTINUE_BTN_STEP_2)

    @allure.step("Register to website and verify that missing or incorrect fields have warnings - step 2.")
    def register_step_2_invalid_data(self):

        self.click(self.DATEOFBIRTH)
        self.fill_text(self.DATEOFBIRTH, ValueEnums.BOGUS_DOB.value)
        self.delete_with_keys(self.DATEOFBIRTH, 1)
        self.click(self.STREET)
        self.fill_text(self.STREET, ValueEnums.INVALID_DATA.value)
        self.delete_with_keys(self.STREET, len(str(ValueEnums.INVALID_DATA.value)))
        self.fill_text(self.POSTCODE, ValueEnums.INVALID_DATA.value)
        self.delete_with_keys(self.POSTCODE, len(str(ValueEnums.INVALID_DATA.value)))
        self.fill_text(self.CITY, ValueEnums.INVALID_DATA.value)
        self.delete_with_keys(self.DATEOFBIRTH, len(str(ValueEnums.INVALID_DATA.value)))

        self.is_warning_visible(self.BIRTHDATE_WARNING)
        self.is_warning_visible(self.STREET_WARNING)
        self.is_warning_visible(self.POSTCODE_WARNING)

        self.scroll_down()

        status = self.is_elem_enabled(self.CONTINUE_BTN_STEP_1)
        baseAssertions.assertEquals(False, status)

    @allure.step("Enter sms code to finish registration - step 3.")
    def register_step_3(self):
        self.fill_text(self.SMS_CODE, ValueEnums.SMS_CODE.value)
        time.sleep(1)
        self.click(self.VERIFY_SMS_BTN)

    @allure.step("Deposit and play registration")
    def register_with_deposit_and_play(self, userdata, amount):

        self.click(self.REGISTER_DEPOSIT_AND_PLAY)
        self.fill_text(self.PAY_AND_PLAY_AMOUNT, amount)
        self.click(self.START_PLAYING)
        self.switch_to_iframe(self.BANKS_IFRAME)
        self.click(self.NORDEA_BANK)
        time.sleep(1)
        self.wait_for_element(self.JATKA_BUTTON, max_retries=10)
        self.click(self.JATKA_BUTTON)
        time.sleep(1)
        self.scroll_down()
        time.sleep(1)
        self.wait_for_element(self.JATKA_BUTTON, max_retries=10)
        self.click(self.JATKA_BUTTON)
        self.click(self.LOGIN_ID)
        self.type_with_keys(self.LOGIN_ID, userdata.userName)
        time.sleep(1)
        self.wait_for_element(self.JATKA_BUTTON, max_retries=10)
        self.click(self.JATKA_BUTTON)
        OTP = self.get_text(self.ONE_TIME_CODE)
        self.click(self.ONE_TIME_CODE_BOX)
        self.type_with_keys(self.ONE_TIME_CODE_BOX, OTP)
        time.sleep(1)
        self.wait_for_element(self.JATKA_BUTTON, max_retries=10)
        self.click(self.JATKA_BUTTON)
        time.sleep(1)
        self.wait_for_element(self.CHECKING_ACCOUNT, max_retries=10)
        self.click(self.CHECKING_ACCOUNT)
        self.wait_for_element(self.LAST_JAKTA_BUTTON, max_retries=10)
        self.click(self.LAST_JAKTA_BUTTON)
        OTP = self.get_text(self.ONE_TIME_CODE)
        self.click(self.ONE_TIME_CODE_BOX)
        self.type_with_keys(self.ONE_TIME_CODE_BOX, OTP)
        self.click(self.CONTINUE_PNP)
        self.switch_to_mainframe()
        self.wait_for_element(self.EMAIL_PAY_N_PLAY, max_retries=10)
        self.fill_text(self.EMAIL_PAY_N_PLAY, userdata.email)
        self.fill_text(self.PASSWORD_PAY_N_PLAY, userdata.password)
        self.fill_text(self.PHONE_PAY_N_PLAY, userdata.phone)
        self.click(self.AGREE_ALL_PAY_N_PLAY)
        self.click(self.REGISTER_PAY_N_PLAY)

    @allure.step("Get page title")
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Clicking country from drop down.")
    def get_country(self, countryCode):
        country_list_number = self.COUNTRYCODE_DICT.get(countryCode)
        COUNTRY_CODE = (By.XPATH, "//*[@id=\"menu-\"]/div[3]/ul/li[" + str(country_list_number) + "]/div/span")
        return COUNTRY_CODE

    @allure.step("Clicking agreements.")
    def click_agreements(self, agreement_combination):

        type_dict = {'termsAndConditions': self.AGREE_TERMS,
                     'cookiePolicy': self.AGREE_COOKIE,
                     'agreeAll': self.AGREE_ALL,
                     'offers': self.AGREE_OFFERS}

        for agr_type in agreement_combination.split(" "):
            self.click(type_dict.get(agr_type))
            time.sleep(0.5)

    def select_for_mobile(self):
        self.click(self.CONTINUE_BTN_STEP_1)
        time.sleep(1)
        self.click(self.CONTINUE_BTN_STEP_1)

    @allure.step("Checking if continue button is enabled.")
    def is_continue_button_enabled(self):
        return self.is_elem_enabled(self.CONTINUE_BTN_STEP_2)

    @allure.step("Check that field warning is displayed {element}")
    def is_warning_visible(self, element):
        status = self.is_elem_displayed(element)
        baseAssertions.assertEquals(True, status)
