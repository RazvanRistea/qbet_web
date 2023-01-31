from allure import step
from api_resources.api_steps.aws_login import LoginAws
from api_resources.controllers.adminEndpointController import AdminController
from api_core.microservices.apibase.assertions.userAssertions import BaseAssertions
from datetime import datetime
import time


class Admin:

    @step("Admin api call to get list of users in cronological order of registration.")
    def getUsers(self, idToken=None, limit=None, position=None, type=None, userData=None):

        """
        We do not initialize the class to get aws login in __INIT__ because if token is passed  we will have one
        less initialization
        """

        def checkValues():
            wait_for_user_creation()
            if 'AUTOTEST' in newGetUsers[0]['firstName']:
                checkUser()
            else:
                checkUserPnp()

        def wait_for_user_creation(max_retries=5):
            retries = 0
            while True:
                try:
                    BaseAssertions().assertEquals(userData.email, newGetUsers[0]['email'])
                    break
                except:
                    print("Button not interactable yet, retrying...")
                    time.sleep(2)
                    retries += 1
                    if retries >= max_retries:
                        print("Max retries reached, stopping.")
                        break

        if idToken is None:
            newLoginAws = LoginAws()
            idToken = newLoginAws.getAwsToken()
        if limit is None:
            limit = 20
        if position is None:
            position = 0
        if type is None:
            type = 'FULL'

        params = {'limit': limit, 'position': position, 'type': type}

        # Get user list
        newGetUsers = AdminController().getUsers(params=params, idToken=idToken)

        @step("Verify user data in BE.")
        def checkUser():

            wait_for_user_creation()
            userdataDob = userData.dateOfBirth
            userdataDatetime = str(datetime.strptime(userdataDob, '%d%m%Y'))

            BaseAssertions().assertEquals(userData.email, newGetUsers[0]['email'])
            BaseAssertions().assertEquals(userData.firstName, newGetUsers[0]['firstName'])
            BaseAssertions().assertEquals(userData.lastName, newGetUsers[0]['lastName'])
            BaseAssertions().assertEquals(userData.postCode, newGetUsers[0]['postCode'])
            BaseAssertions().assertContains(str(newGetUsers[0]['mobilePhone']), str(userData.phone))
            BaseAssertions().assertContains(userdataDatetime, newGetUsers[0]['dateOfBirth'])
            BaseAssertions().assertEquals(userData.street, newGetUsers[0]['street'])
            BaseAssertions().assertEquals(userData.city, newGetUsers[0]['city'])
            BaseAssertions().assertEquals(False, newGetUsers[0]['pnpMade'])

        @step("Verify user data in BE for pnp.")
        def checkUserPnp():

            wait_for_user_creation()
            BaseAssertions().assertEquals(userData.email, newGetUsers[0]['email'])
            BaseAssertions().assertEquals(True, newGetUsers[0]['pnpMade'])
            BaseAssertions().assertContains(str(newGetUsers[0]['mobilePhone']), str(userData.phone))

        checkValues()
