import requests
import os
import shutil
import json


class AllureReport(Exception):

    def login(self):

        url = "http://allure.dev.ibet.com:7272/allure-docker-service/login"

        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json'
        }

        data = {"username": "admin", "password": "HGJHdfjkTjj(977"}

        response = requests.request("POST", url, headers=headers, json=data)

        if response.status_code != 200:
            raise AllureReport("Could not log in")

        token = response.cookies.get_dict()['csrf_access_token']
        cookie = response.cookies.get_dict()['access_token_cookie']

        return token, cookie

    def getfiles(self):

        data = []
        files = os.listdir(os.path.dirname(os.path.realpath(__file__)) + "/web_tests/allure-results")

        files = [i for i in files if os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + "/web_tests/allure"
                                                                                                  "-results" + '/' +
                                                    i)]
        for file in files:
            file = (
            'files[]', (file, open(os.path.dirname(os.path.realpath(__file__)) + f'/web_tests/allure-results/{file}', 'rb'), 'application/json'))
            data.append(file)
        return data

    def sendresults(self, data, token, accsess_token):

        url = "http://allure.dev.ibet.com:7272/allure-docker-service/send-results"
        params = {
            'project_id': 'ibet-green',
        }
        payload = {}
        files = data
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'X-CSRF-TOKEN': f'{token}',
            'Cookie': f'access_token_cookie={accsess_token}'}

        response = requests.request("POST", url, headers=headers, data=payload, files=files, params=params)

        if response.status_code != 200:
            raise AllureReport("could not call send results")

        jsonResponse = response.json()

        return jsonResponse

    def generatereport(self, token, accsess_token):

        url = "http://allure.dev.ibet.com:7272/allure-docker-service/generate-report"

        params = {
            'project_id': 'ibet-green',
            'execution_name': 'Allure%20Docker%20Service%20UI'
        }

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'X-CSRF-TOKEN': f'{token}',
            'Cookie': f'access_token_cookie={accsess_token}'}

        response = requests.request("GET", url, headers=headers, params=params)

        if response.status_code != 200:
            raise AllureReport("Could not generate report")

        jsonResponse = response.json()

        url = jsonResponse["data"]["report_url"]

        return response.status_code, url

    def getgitlabtoken(self):
        pipelineid = os.environ['PIPELINEID']
        branch = os.environ['BRANCH']
        return branch, pipelineid


def reporting():
    reportingtool = AllureReport()
    login = reportingtool.login()
    token = login[0]
    cookie = login[1]
    data = reportingtool.getfiles()

    reportingtool.sendresults(data, token, cookie)
    report_response = reportingtool.generatereport(token, cookie)

    if report_response[0] == 200:
        print("Result has been published to: {}".format(report_response[1]))

    return report_response[1]

