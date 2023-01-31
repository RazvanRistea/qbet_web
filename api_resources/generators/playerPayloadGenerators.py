from faker import Faker

from api_core.util.configManager import ConfigManager
from allure import step
from data.data_generator import UserDataGenerator

import uuid
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


class PlayerPayloadGenerator:

    def __init__(self):
        newUserGenerator = UserDataGenerator()
        self.newUserData = newUserGenerator.generateSignupData()
        self.faker = Faker()

    @step("Create payload for new user registration step one.")
    def registrationStepOne(self, firstName=None, lastName=None, email=None, mobilePhone=None, password=None):

        if firstName is None:
            firstName = self.newUserData.firstName
        if lastName is None:
            lastName = self.newUserData.lastName
        if email is None:
            email = self.newUserData.email
        if password is None:
            password = self.newUserData.password
        if mobilePhone is None:
            mobilePhone = self.newUserData.phone

        payload = {
            "firstName": f"{firstName}",
            "lastName": f"{lastName}",
            "email": f"{email}",
            "mobilePhone": "+358" + f"{mobilePhone}",
            "password": f"{password}"
        }

        return json.dumps(payload)

    @step("Create payload for new user registration step two.")
    def registrationStepTwo(self, dateOfBirth=None, postCode=None, city=None, street=None, playerId=None):

        if dateOfBirth is None:
            dateOfBirth = self.faker.date_between_dates(date_start=datetime(1930, 1, 1),
                                                        date_end=datetime.now() - relativedelta(years=18))
        if postCode is None:
            postCode = self.newUserData.postCode
        if city is None:
            city = self.newUserData.city
        if street is None:
            street = self.newUserData.street

        payload = {
            "playerId": playerId,
            "currencyCode": "EUR",
            "gender": "m",
            "street": f"{street}",
            "city": f"{city}",
            "marketingOptIn": True,
            "cookiePolicyAccepted": True,
            "allConditions": True,
            "mediaTag": None,
            "provinceCode": None,
            "termsAndConditionsAcceptedVersion": 5,
            "dateOfBirth": f"{dateOfBirth}",
            "postalCode": f"{postCode}",
            "countryCode": "FI",
            "termsAndConditionsAccepted": True,
            "languageCode": "en"
        }

        return json.dumps(payload)

    @step("Create sms request payload")
    def requestSms(self, playerId=None):

        payload = {
            "playerId": playerId
        }

        return json.dumps(payload)

    @step("Send SMS verification payload")
    def verifySms(self, playerId=None):

        payload = {"playerId": playerId, "password": "QAPassword1!", "code": "1111"}

        return json.dumps(payload)

    @step("Get pariplay token")
    def paripalyToken(self):

        payload = {
            "GameCode": "PP_HTML5_StallionFortunes96",
            "CurrencyCode": "EUR",
            "LanguageCode": "en-FI",
            "PlayerIP": "202.166.129.78"
        }

        return json.dumps(payload)

    @step("Pariplay authentication")
    def authPariplay(self, playerId=None, token=None):

        payload = {
            "PlayerId": playerId,
            "PlatformType": 3,
            "Token": token,
            "Account": {
                "UserName": "ibet",
                "Password": "ibet123!"
            },
            "BrandId": None
        }

        return json.dumps(payload)

    @step("Pariplay credit")
    def pariplayCredit(self, playerId=None, token=None, roundId=None, txsId=None, amount=None):

        if txsId is None:
            txsId = str(uuid.uuid4())
        if amount is None:
            amount = 100
        if roundId is None:
            playerId = str(uuid.uuid4())

        payload = {
            "Account": {
                "UserName": "ibet",
                "Password": "ibet123!"
            },
            "Token": token,
            "GameCode": "PP_HTML5_AesirTreasures96",
            "PlayerId": playerId,
            "RoundId": roundId,
            "TransactionId": txsId,
            "Amount": amount,
            "CreditType": "NormalWin",
            "EndGame": True,
            "Feature": "Normal"
        }

        return json.dumps(payload)

    @step("Pariplay debit")
    def pariplayDebit(self, playerId=None, token=None, roundId=None, txsId=None, amount=None):

        if txsId is None:
            txsId = str(uuid.uuid4())
        if amount is None:
            amount = 100

        payload = {
            "GameCode": "PP_HTML5_AesirTreasures96",
            "PlayerId": playerId,
            "RoundId": roundId,
            "TransactionId": txsId,
            "Amount": amount,
            "Taxes": None,
            "EndGame": False,
            "Feature": "Normal",
            "FeatureId": None,
            "FeatureAmount": None,
            "TransactionConfiguration": None,
            "TicketAmount": None,
            "JackpotContribution": None,
            "JackpotDetailsParameters": None,
            "RoomId": None,
            "IsBingo": None,
            "Token": token,
            "Account": {
                "UserName": "ibet",
                "Password": "ibet123!"
            },
            "BrandId": None
        }

        return json.dumps(payload)
