import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from api_core.microservices.apibase.assertions.userAssertions import BaseAssertions

baseAssertions = BaseAssertions()


class AboutPage(BasePage):
    """ About page - The first page that appears when navigating to base URL"""
    LOGIN_LINK = (By.XPATH, '//*[@id="root"]/header/div/div/div/div[3]/div/button/span[1]')
    REGISTER_LINK = (By.XPATH, '//*[@id="root"]/header/div/div/div/div[4]/button')
    COOKIE_POP_UP_OK_BUTTON = (By.XPATH, '//*[@id="root"]/div[8]/div/div[2]/div[2]/button/span[1]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click Login link")
    def click_login_link(self):
        self.click(self.LOGIN_LINK)

    @allure.step("I click on the registration button.")
    def click_register_link(self):
        self.click(self.REGISTER_LINK)

    @allure.step("I click on the OK cookies button pop up to close it.")
    def click_cookie_pop_up_ok_btn(self):
        BasePage.click(self, self.COOKIE_POP_UP_OK_BUTTON)

    @allure.step("Checking if user is not logged in.")
    def user_is_not_logged_in(self):
        status = self.is_elem_enabled(self.REGISTER_LINK)
        baseAssertions.assertEquals(True, status)
