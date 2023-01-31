from faker import Faker
from allure import step
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
import inspect
import json
from collections import namedtuple


class UserDataGenerator:

    # Generate unique data for the sign-up function and return a dictionary with all the required fields
    @step("Generating used date all data is random except the arguments that are passed")
    def generateSignupData(self, userName=None, firstName=None, lastName=None, email=None, password=None, phone=None,
                           dateOfBirth=None, street=None, postCode=None, city=None, countryCode=None):

        faker = Faker()

        if userName is None:
            userName = (faker.first_name()).lower() + str(faker.pyint(1, 1000))

        if firstName is None:
            firstName = "AUTOTEST" + faker.first_name()

        if lastName is None:
            lastName = faker.last_name()

        if email is None:
            email = "qarrbet+" + str(faker.pyint(10000, 99999)) + "@gmail.com"

        if password is None:
            password = "QAPassword1!"

        if phone is None:
            phone = faker.pyint(1000000, 9999999)

        if dateOfBirth is None:
            dateOfBirth = faker.date_between_dates(date_start=datetime(1930, 1, 1),
                                                   date_end=datetime.now() - relativedelta(years=18)).strftime("%d%m%Y")

        if street is None:
            street = faker.street_name()

        if city is None:
            city = faker.city()

        if postCode is None:
            postCode = faker.postcode()

        userSignUpDict = {'userName': userName, 'firstName': firstName, 'lastName': lastName, 'email': email,
                          'password': password, 'phone': phone, 'dateOfBirth': dateOfBirth, 'street': street,
                          'city': city, 'postCode': postCode, 'countryCode': countryCode}

        userSignUpDict = json.loads(json.dumps(userSignUpDict),
                                    object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        return userSignUpDict
