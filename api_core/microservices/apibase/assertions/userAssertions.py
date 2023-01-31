from allure import step
from assertpy import soft_assertions, assert_that


class BaseAssertions:
    @step("Assert Message equals.")
    def assertEquals(self, actual, expected):
        with soft_assertions():
            assert_that(actual).is_equal_to(expected)

    @step("Assert Message not equals.")
    def assertNotEqual(self, actual, expected):
        with soft_assertions():
            assert_that(actual).is_not_equal_to(expected)

    @step("Assert Message contains.")
    def assertContains(self, actual, expected):
        with soft_assertions():
            assert_that(actual).contains(expected)
