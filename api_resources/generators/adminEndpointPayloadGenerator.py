from api_core.util.configManager import ConfigManager
from allure import step
from faker import Faker
import json

class AdminAPICallPayloadGenerator:

    @step("sth")
    def generatePayload(self, sth=None):

        faker = Faker()

        if sth is None:
            sth = faker.sth()
        if sth is None:
            sth = faker.sth()
        if sth is None:
            sth = faker.pyint()

        if sth is None:
            payload = {
            "sth": "{}".format(sth),
            "sth": "{}".format(sth),
            "sth": "{}".format(sth)
            }
        else:
            payload = {
            "sth": "{}".format(sth),
            "sth": "{}".format(sth),
            "sth": "{}".format(sth)
            }

        return json.dumps(payload)

