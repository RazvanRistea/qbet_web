import logging
from datetime import datetime

import allure
import requests
from allure_commons import plugin_manager
from allure_commons.model2 import TestResult
from pytest import fixture, hookimpl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from api_core.microservices.apibase.assertions.userAssertions import BaseAssertions
from api_resources.api_steps.admin_steps import Admin
from api_resources.controllers.adminEndpointController import AdminController
from api_resources.controllers.cognitoLoginController import CognitoController
from api_resources.generators.cognitoPayloadGenerator import CongnitoPayoloadGenerator
from data.data_generator import UserDataGenerator
from helper_enums.help_enums import Enums
from pages.about_page import AboutPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.registration_page import RegistrationPage
from utils.config_parser import ConfigParserIni

logger = logging.getLogger("FIXTURE")
# instantiations
baseAssertions = BaseAssertions()
userDataGenerator = UserDataGenerator()
cognitoPayloadGenerator = CongnitoPayoloadGenerator()
cognitoController = CognitoController()
adminController = AdminController()
adminSteps = Admin()


# reads parameters from pytest command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser that the automation will run in")


@fixture
def browser(request):
    return request.config.getoption("--browser")


def get_public_ip():
    return requests.get("http://checkip.amazonaws.com").text.rstrip()


@fixture(scope="session")
def prep_properties():
    return ConfigParserIni("props.ini")


# https://stackoverflow.com/a/61433141/4515129
@fixture
# Instantiates Page Objects
def pages():
    about_page = AboutPage(driver)
    login_page = LoginPage(driver)
    registration_page = RegistrationPage(driver)
    forgot_password_page = ForgotPasswordPage(driver)

    return locals()


# Write to allure environment removed due to causing errors will add back when i fix it and get proper repo
@fixture(autouse=True)
def create_driver(prep_properties, request):  # ,write_allure_environment):
    global browser, base_url, driver
    browser = request.config.getoption("--browser")
    base_url = prep_properties.config_section_dict("Base Cfg")["base_url"]

    """ Might Never Use Firefox, but still nice to have."""
    if browser == "firefox":  # will never use this, probly
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == Enums.HEADLESS.value:

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--no-sandbox')
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        driver = webdriver.Remote(
            command_executor=Enums.CHROME_PIPELINE.value,
            desired_capabilities=chrome_options.to_capabilities())

    elif browser == Enums.MOBILE.value:
        mobile_emulation = {

            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},

            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, "
                         "like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    driver.implicitly_wait(5)

    driver.get(base_url)
    yield
    if request.node.rep_call.failed:
        screenshot_name = f"screenshot on failure: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}"
        allure.attach(body=driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        allure.attach(body=get_public_ip(), name="public ip address", attachment_type=allure.attachment_type.TEXT)
    driver.quit()


def custom_write_test_case(self, uuid=None):
    test_result = self._pop_item(uuid=uuid, item_type=TestResult)
    if test_result:
        if test_result.parameters:
            adj_parameters = []
            for param in test_result.parameters:
                if param.name != '_pytest_bdd_example':
                    # do not include parameters with "_pytest_bdd_example"
                    adj_parameters.append(param)
            test_result.parameters = adj_parameters

        plugin_manager.hook.report_result(result=test_result)


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, f"rep_{rep.when}", rep)


# BDD Fixtures
@fixture(scope='function')
def context():
    return {}


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
