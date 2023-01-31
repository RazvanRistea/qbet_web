import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TopMenuBar(BasePage):
    """Top menu bar - The bar that appears on the top of the page prior to login """
    LOGIN_LINK = (By.XPATH, '//*[@id="root"]/header/nav/div[3]/button[1]')
    REGISTER_LINK = (By.XPATH, '//*[@id="root"]/header/nav/div[3]/button[2]')
    SPORTS_BUTTON = (By.XPATH, '//*[@id="root"]/header/nav/div[2]/button[1]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click Login button")
    def click_login(self):
        self.click(self.LOGIN_LINK)

    @allure.step("Click Register button")
    def click_register(self):
        self.click(self.REGISTER_LINK)

    @allure.step("Click Sports button")
    def click_sports(self):
        self.click(self.SPORTS_BUTTON)
