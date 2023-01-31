from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BasePage:
    """ Wrapper for selenium operations """

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def getPage(self, page):
        self._driver.get(page)

    def refresh(self):
        self._driver.refresh()

    def delete_with_keys(self, webelement, length):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        actions = ActionChains(self._driver)
        for i in range(length):
            actions.send_keys(Keys.BACKSPACE)
            actions.perform()

        self._highlight_element(el, "green")

    def type_with_keys(self, webelement, text):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        self._highlight_element(el, "green")

        actions = ActionChains(self._driver)
        actions.send_keys(text)
        actions.perform()

    def click(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        self._highlight_element(el, "green")
        el.click()

    def fill_text(self, webelement, txt):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()
        self._highlight_element(el, "green")
        el.send_keys(txt)

    def get_element(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        actions = ActionChains(self._driver)
        actions.move_to_element(el).perform()
        self._highlight_element(el, "green")

    def clear_text(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        self._highlight_element(el, "green")
        el.clear()

    def scroll_to_bottom(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down(self):
        actions = ActionChains(self._driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        time.sleep(2)  # this adds some time but it is best to leave some sleep even a big one to be sure

    def scroll_up(self):
        actions = ActionChains(self._driver)
        actions.send_keys(Keys.PAGE_UP)
        actions.perform()
        time.sleep(2)  # this adds some time but it is best to leave some sleep even a big one to be sure

    def submit(self, webelement):
        self._highlight_element(webelement, "green")
        webelement.submit()

    def get_text(self, webelement):
        el = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
        self._highlight_element(el, "green")
        return el.text

    def move_to_element(self, webelement):
        action = ActionChains(self._driver)
        self._wait.until(expected_conditions.visibility_of(webelement))
        action.move_to_element(webelement).perform()

    def is_elem_displayed(self, webelement):
        webelement = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
        try:
            return webelement.is_displayed()
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    def is_elem_enabled(self, webelement):
        el = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
        return el.is_enabled()

    def switch_to_iframe(self, webelement):
        iframe = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
        self._driver.switch_to.frame(iframe)

    def switch_to_mainframe(self):
        self._driver.switch_to.default_content()

    def wait_for_element(self, webelement, max_retries):
        retries = 0
        while True:
            try:
                el = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
                break
            except:
                print("Button not interactable yet, retrying...")
                time.sleep(2)
                retries += 1
                if retries >= max_retries:
                    print("Max retries reached, stopping.")
                    break

    def _highlight_element(self, webelement, color):
        original_style = webelement.get_attribute("style")
        new_style = f"background-color:yellow;border: 1px solid {color}{original_style}"
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style + "');},0);", webelement)
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style + "');},400);", webelement)
