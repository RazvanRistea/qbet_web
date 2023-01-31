from api_core.util.configManager import ConfigManager
from api_core.microservices.restBase import ApiClient
from allure import step

adminEndpointHeaders = {
    'content-type': 'application/x-amz-json-1.1',
    'authority': str(ConfigManager.getConfig('COGNITOQBETADMIN', 'AUTHORITY')),
    'x-amz-target': ConfigManager.getConfig('COGNITOQBETADMIN', 'X-AMZ-TARGET'),
    'x-amz-user-agent': ConfigManager.getConfig('COGNITOQBETADMIN', 'X-AMZ-USER-AGENT')
}


class CognitoController(ApiClient):

    @step("Get IdToken.")
    def postGetIdToken(self, payload=None):
        path = ConfigManager.getConfig('COGNITOQBETADMIN', 'ENDPOINTTOKENID')
        response = super().post(base_address=ConfigManager.getConfig('COGNITOQBETADMIN', 'URL'),
                                path=path, data=payload,
                                headers=adminEndpointHeaders)

        return response.json()

    @step("Get IdToken for player.")
    def postGetIdTokenPlayer(self, payload=None):
        path = ConfigManager.getConfig('COGNITOQBETPLAYER', 'ENDPOINTTOKENID')
        response = super().post(base_address=ConfigManager.getConfig('COGNITOQBETPLAYER', 'URL'),
                                path=path, data=payload,
                                headers=adminEndpointHeaders)

        return response.json()
