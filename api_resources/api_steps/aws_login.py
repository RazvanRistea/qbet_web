from api_resources.generators.cognitoPayloadGenerator import CongnitoPayoloadGenerator
from api_resources.controllers.cognitoLoginController import CognitoController
from api_resources.generators.cognitoPayloadGeneratorPlayer import CongnitoPayoloadGeneratorPlayer
from allure import step



class LoginAws:

    @step("Login to AWS and get IdToken for other API Calls.")
    def getAwsToken(self):

        newLoginPayload = CongnitoPayoloadGenerator().cognitoPayloadGenerator()
        newAwsLogin = CognitoController().postGetIdToken(payload=newLoginPayload)

        idToken = newAwsLogin['AuthenticationResult']['IdToken']

        return idToken

    @step("Login to AWS and get IdToken for other API Calls for player site.")
    def getAwsTokenPlayer(self, password=None, username=None):
        newLoginPayload = CongnitoPayoloadGeneratorPlayer().cognitoPayloadGenerator(password=password,
                                                                                    username=username)
        newAwsLogin = CognitoController().postGetIdTokenPlayer(payload=newLoginPayload)

        idToken = newAwsLogin['AuthenticationResult']['IdToken']

        return idToken
