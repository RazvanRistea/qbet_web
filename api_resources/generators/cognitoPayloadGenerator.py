from api_core.util.configManager import ConfigManager
from allure import step
from api_core.util.cognito.cognitoAws import AwsCognito
import json


class CongnitoPayoloadGenerator:

    def __init__(self):
        newAwsCognito = AwsCognito()
        self.token = newAwsCognito.getAwsToken()

    @step("Generateing Cognito get IdToken payload")
    def cognitoPayloadGenerator(self):
        payload = {"ClientId": f"{ConfigManager.getConfig('COGNITOQBETADMIN', 'CLIENTID')}",
                   "AuthFlow": "REFRESH_TOKEN_AUTH",
                   "AuthParameters": {
                       "REFRESH_TOKEN": f"{self.token}",
                       "DEVICE_KEY": None}}

        return json.dumps(payload)
