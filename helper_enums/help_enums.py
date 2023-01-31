from enum import Enum


class Enums(Enum):
    CHROME_PIPELINE = "http://chrome:4444"
    MOBILE = "chrome_mobile"
    HEADLESS = "chrome_headless"


class ValueEnums(Enum):
    SMS_CODE = "1111"
    BOGUS_VALUE = "bogus"
    BOGUS_DOB = 9
    INVALID_DATA = "#!$"
    INVALID_EMAIL = "invalid_email_rr@test.com"
    INVALID_PASSWORD = "2#2$"


class UserData(Enum):
    qbet_email = "qbetExisting@testautomation.com"
    qbet_password = "Parola$123"
    invalid_email = "$21421"
    invalid_password = "NOTWORKING"
    ibet_email = "ibetExisting@testautomation.com"
    ibet_password = "Parola$123"
