from allure import step
import json
from collections import namedtuple

from api_resources.controllers.playerEndpointController import PlayerController
from api_core.microservices.apibase.assertions.userAssertions import BaseAssertions
from api_resources.generators.playerPayloadGenerators import PlayerPayloadGenerator
from api_resources.api_steps.aws_login import LoginAws


class Player:

    def __init__(self):
        self.newPayloadGen = PlayerPayloadGenerator()
        self.newPlayerController = PlayerController()

    @step("Api calls to register a new user.")
    def registerNewUser(self):
        payload_step_one = self.newPayloadGen.registrationStepOne()
        register_user_step_one = self.newPlayerController.registerStepOne(payload=payload_step_one)

        payload_step_two = self.newPayloadGen.registrationStepTwo(playerId=register_user_step_one["playerId"])
        register_user_step_two = self.newPlayerController.registerStepTwo(payload=payload_step_two)

        payload_step_one = json.loads(payload_step_one)
        payload_step_two = json.loads(payload_step_two)

        sms_request_playload = self.newPayloadGen.requestSms(playerId=register_user_step_one["playerId"])
        sms_request = self.newPlayerController.requestSMS(payload=sms_request_playload)

        sms_verification_payload = self.newPayloadGen.verifySms(playerId=register_user_step_one["playerId"])
        sms_verification = self.newPlayerController.verifySMS(payload=sms_verification_payload)

        @step("Verify user data has been created.")
        def checkUser():
            BaseAssertions().assertEquals(sms_request.status_code, 200)
            BaseAssertions().assertEquals(sms_verification.status_code, 200)
            BaseAssertions().assertEquals(payload_step_one['email'], register_user_step_two['email'])
            BaseAssertions().assertEquals(payload_step_one['firstName'], register_user_step_two['firstName'])
            BaseAssertions().assertEquals(payload_step_one['lastName'], register_user_step_two['lastName'])
            BaseAssertions().assertEquals(payload_step_two['postalCode'], register_user_step_two['postCode'])
            BaseAssertions().assertEquals(payload_step_one['mobilePhone'], register_user_step_two['mobilePhone'])
            BaseAssertions().assertEquals(payload_step_two['street'], register_user_step_two['street'])
            BaseAssertions().assertEquals(payload_step_two['city'], register_user_step_two['city'])

        checkUser()

        user = {'playerId': register_user_step_two['playerId'], 'email': register_user_step_two['email'],
                'password': payload_step_one['password']}

        user = json.loads(json.dumps(user),
                          object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        return user

    @step("Api call to player api to get player balance")
    def getBalance(self, idToken=None, password=None, username=None):
        """
        We do not initialize the class to get aws login in __INIT__ because if token is passed  we will have one
        less initialization
        """
        if password is None:
            password = "QAPassword1!"

        if idToken is None:
            newLoginAws = LoginAws()
            idToken = newLoginAws.getAwsTokenPlayer(password=password, username=username)

        # Get user balance

        user_data = PlayerController().getBalance(idToken=idToken)
        user_data = json.loads(json.dumps(user_data),
                               object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        return user_data.MAIN[0].balance


# player = Player()
# print(player.registerNewUser())
