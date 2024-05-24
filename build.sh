#!/usr/bin/env bash

# test 文件名必须以 test_ 开头，否则会找不到
TestDir="./testcases"
ReportDir="./.build/allure-report"
ResultDir="./.build/allure-results"
Environment="./.build/environment"

/Users/shiying/PycharmProjects/testSY0517/environment.xml

#set -xe

python main.py "$TestDir" $ResultDir
cp /Users/shiying/PycharmProjects/testSY0517/environment.xml ReportDir

#allure generate --clean -o $ReportDir $ResultDir
allure generate -o $ReportDir $ResultDir
#allure serve ./.build/allure-report
