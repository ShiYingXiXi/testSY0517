#!/usr/bin/env bash

# test 文件名必须以 test_ 开头，否则会找不到
TestDir="./testcases"
ReportDir="./.build/allure-report"
ResultDir="./.build/allure-results"

set -xe

python main.py "$TestDir" $ResultDir

allure generate --clean -o $ReportDir $ResultDir

#allure generate  -o $ReportDir $ResultDir
