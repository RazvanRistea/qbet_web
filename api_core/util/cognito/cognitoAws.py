import boto3
from dotenv import load_dotenv
from api_core.util.configManager import ConfigManager
from allure import step


class AwsCognito:

    @step("Get cognito token")
    def getAwsToken(self):
        load_dotenv()

        client = boto3.client('cognito-idp', region_name=ConfigManager.getConfig('COGNITOQBETADMIN', 'REGION'))
        response = client.initiate_auth(
            ClientId=ConfigManager.getConfig('COGNITOQBETADMIN', 'CLIENTID'),
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': ConfigManager.getConfig('COGNITOQBETADMIN', 'USERNAME'),
                'PASSWORD': ConfigManager.getConfig('COGNITOQBETADMIN', 'PASSWORD')
            },
            ClientMetadata={
                "ipAddress": "188.26.14.36",
                "country": "",
                "blackbox": ""
            }
        )
        # we might use this for something
        token = response['AuthenticationResult']['AccessToken']
        refresh_token = response['AuthenticationResult']['RefreshToken']

        return refresh_token
