#!/bin/sh
echo Waiting for test initialization ...
echo $1 was selected as the selenium node.
#sleep 15

cd web_tests
pytest --alluredir=allure-results --browser $1 --log-cli-level=INFO

if [[ $? == 0 ]]; then
        cd ..
        echo ALL TESTS PASSED! Please check test results on the generated report url.
        REPORT=$(python -c 'import allureResultsHelper; allureResultsHelper.reporting()')
        echo $REPORT
      else
        cd ..
        REPORT=$(python -c 'import allureResultsHelper; allureResultsHelper.reporting()')
        echo TEST FAILURE CHECK TEST LOGS!!! Please generate test report from test results on on the generated report url.
        echo $REPORT
        exit 1;
fi
