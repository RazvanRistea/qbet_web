from api_core.util.configManager import ConfigManager
from allure import step
from api_core.util.cognito.playerCognitoAws import PlayerAwsCognito
import json


class CongnitoPayoloadGeneratorPlayer:

    def __init__(self):
        self.token = None
        self.newAwsCognito = PlayerAwsCognito()

    @step("Generateing Cognito get IdToken payload")
    def cognitoPayloadGenerator(self, password, username):
        self.token = self.newAwsCognito.getAwsToken(password=password, username=username)
        payload = {"ClientId": f"{ConfigManager.getConfig('COGNITOQBETPLAYER', 'CLIENTID')}",
                   "AuthFlow": "REFRESH_TOKEN_AUTH",
                   "AuthParameters": {
                       "REFRESH_TOKEN": f"{self.token}",
                       "DEVICE_KEY": None}}

        return json.dumps(payload)


