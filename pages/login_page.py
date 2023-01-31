import allure
from selenium.webdriver.common.by import By
import time
from pages.top_bars.top_menu_bar import TopMenuBar
from helper_enums.help_enums import UserData


class LoginPage(TopMenuBar):
    """ Login Page """
    USERNAME_FIELD = (By.XPATH, "//*[@id=\"email\"]")
    PASSWORD_FIELD = (By.XPATH, "//*[@id=\"password\"]")
    LOGIN_BUTTON = (By.XPATH, "//*[@id=\"root\"]/header/div/div/div/div[3]/div/div/div/div[2]/section/div/div[1]/button")

    PAGE_TITLE = (By.XPATH, "//*[@id=\"root\"]/header/div/div/div/div[3]/div/div/div/div[1]/div/div/div/h5")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//*[@id=\"root\"]/header/div/div/div/div[3]/div/div/div/div["
                                      "2]/section/div/div[2]/button/span[1]")
    MAIN_MENU_TOP_BAR = (By.XPATH, "//*[@id=\"root\"]/header/div/div/div/div[4]/span/button/span[1]/span[2]")
    WRONG_CREDS_ERROR = (By.XPATH, "//*[@id=\"root\"]/header/div/div/div/div[3]/div/div/div/div[2]/section/div/div[1]/p")
    ENTER_VALID_EMAIL = (By.XPATH, "//*[@id=\"root\"]/header/div/div/div/div[3]/div/div/div/div["
                                   "2]/section/form/div/div[1]/div/p")

    REGISTER_LINK = (By.XPATH, "//*[@id=\"root\"]/header/div/div/div/div[3]/div/div/div/div["
                               "2]/section/div/button/span[1]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Log in with username and password.")
    def login_user(self, newUserData, password=None):
        email = newUserData.email

        if password is None:
            password = newUserData.password

        self.fill_text(self.USERNAME_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.wait_for_element(self.LOGIN_BUTTON, max_retries=5)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Check if user is logged in.")
    def check_user_logged_in(self):
        self.wait_for_element(self.MAIN_MENU_TOP_BAR, max_retries=7)
        self.is_elem_enabled(self.MAIN_MENU_TOP_BAR)
        self.is_elem_displayed(self.MAIN_MENU_TOP_BAR)

    @allure.step("Get page title")
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    @allure.step("Log in with username and password from new created user.")
    def login_with_ibet_creds(self):
        email = UserData.ibet_email.value
        password = UserData.ibet_password.value

        self.fill_text(self.USERNAME_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.wait_for_element(self.LOGIN_BUTTON, max_retries=5)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Login throws error for password and email")
    def wrong_creds_error(self):
        self.wait_for_element(self.WRONG_CREDS_ERROR, max_retries=7)
        self.is_elem_enabled(self.WRONG_CREDS_ERROR)
        self.is_elem_displayed(self.WRONG_CREDS_ERROR)

    @allure.step("User is promted to enter a valid email adress.")
    def valid_email_error(self):
        self.wait_for_element(self.ENTER_VALID_EMAIL, max_retries=7)
        self.is_elem_enabled(self.ENTER_VALID_EMAIL)
        self.is_elem_displayed(self.ENTER_VALID_EMAIL)

    @allure.step("Log in with invalid credentials.")
    def login_with_invalid_credentials(self):
        email = UserData.invalid_email.value
        password = UserData.invalid_password.value

        self.fill_text(self.USERNAME_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)

    @allure.step("Log in with username and but wrong password from new created user.")
    def login_valid_email_invalid_password(self, newUserData):
        email = newUserData.email
        password = str(UserData.invalid_password)

        self.fill_text(self.USERNAME_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.wait_for_element(self.LOGIN_BUTTON, max_retries=5)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Go to registration menu.")
    def go_to_register(self):

        self.click(self.REGISTER_LINK)

    @allure.step("Go to forgot passsword page.")
    def go_to_forgot_password(self):

        self.click(self.FORGOT_PASSWORD_LINK)
