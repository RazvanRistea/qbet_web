import allure
from selenium.webdriver.common.by import By
import time
from pages.top_bars.top_menu_bar import TopMenuBar
from helper_enums.help_enums import Enums, ValueEnums


class ForgotPasswordPage(TopMenuBar):
    """ Login Page """

    PAGE_TITLE = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div[1]/div/div/h5")
    EMAIL = (By.XPATH, "//*[@id=\"email\"]")
    SEND_CODE = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div[2]/section/button")
    ENTER_CODE = (By.XPATH, "//*[@id=\"pincode-0\"]")
    SEND_CODE_AGAIN = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div[2]/section/div[3]/button/span[1]")
    VERIFY = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div[2]/section/div[2]/button/span[1]")
    SET_PASSWORD = (By.XPATH, "// *[ @ id = \"root\"] / div[2] / div / div / div / div / div / div[2] / section / "
                              "button / "
                              "span[1]")
    PASSWORD = (By.XPATH, "// *[ @ id = \"password\"]")
    PASS_NOT_FOND_ERR = (By.XPATH, "// *[ @ id = \"root\"] / div[2] / div / div / div / div / div / div[2] / section "
                                   "/ div[1] / form / div / div / div / div / div[5] / p")
    CODE_TIMER = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div[2]/section/div[3]/div[2]/h6")
    LOGIN_LINK = (By.XPATH, '//*[@id="root"]/header/nav/div[3]/button[1]')

    PASS_ERR_CHAR = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div["
                               "2]/section/div/form/div/div/div/ul/li[1]")
    PASS_ERR_UPPER = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div["
                                "2]/section/div/form/div/div/div/ul/li[2]")
    PASS_ERR_LOWER = (By.XPATH, "//*[@id=\"root\"]/div[2]/div/div/div/div/div/div["
                                "2]/section/div/form/div/div/div/ul/li[3]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Request SMS code for password reset.")
    def request_password_reset(self, newUserData, invalid=False, request_new_OTP=False):

        if invalid is True:
            email = ValueEnums.INVALID_EMAIL.value
        else:
            email = newUserData.email

        retries = 0
        max_retries = 5
        while retries < max_retries:
            try:
                self.wait_for_element(self.EMAIL, max_retries=5)
                self.click(self.EMAIL)
                self.type_with_keys(self.EMAIL, ".")
                self.delete_with_keys(self.EMAIL, 1)
                self.type_with_keys(self.EMAIL, email)

                self.wait_for_element(self.SEND_CODE, max_retries=5)
                self.click(self.SEND_CODE)
                if request_new_OTP is True:
                    time.sleep(30)
                    self.click(self.SEND_CODE_AGAIN)
                    self.is_elem_displayed(self.CODE_TIMER)
                self.fill_text(self.ENTER_CODE, ValueEnums.SMS_CODE.value)
                self.wait_for_element(self.VERIFY, max_retries=5)
                self.click(self.VERIFY)
                break
            except:
                time.sleep(1)
                self.refresh()
                retries += 1
                if retries == max_retries:
                    raise Exception("Maximum number of retries reached.")

    @allure.step("Set new password")
    def set_new_password(self, newUserData, invalid_password=False):
        if invalid_password is False:
            password = newUserData.password + "New"
            self.click(self.PASSWORD)
            self.fill_text(self.PASSWORD, password)
            self.wait_for_element(self.SET_PASSWORD, max_retries=5)
            self.click(self.SET_PASSWORD)
        else:
            password = ValueEnums.INVALID_PASSWORD.value
            self.click(self.PASSWORD)
            self.fill_text(self.PASSWORD, password)

        return password

    @allure.step("Get page title")
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Check if not found error is shown")
    def check_not_fund_error_is_found(self):
        self.wait_for_element(self.PASS_NOT_FOND_ERR, max_retries=10)
        self.is_elem_enabled(self.PASS_NOT_FOND_ERR)
        self.is_elem_displayed(self.PASS_NOT_FOND_ERR)

    @allure.step("Check if password error is shown")
    def check_wrong_pass_err(self):
        self.wait_for_element(self.PASS_ERR_CHAR, max_retries=10)
        self.is_elem_enabled(self.PASS_ERR_CHAR)
        self.is_elem_displayed(self.PASS_ERR_CHAR)

        self.wait_for_element(self.PASS_ERR_UPPER, max_retries=10)
        self.is_elem_enabled(self.PASS_ERR_UPPER)
        self.is_elem_displayed(self.PASS_ERR_UPPER)

        self.wait_for_element(self.PASS_ERR_LOWER, max_retries=10)
        self.is_elem_enabled(self.PASS_ERR_LOWER)
        self.is_elem_displayed(self.PASS_ERR_LOWER)