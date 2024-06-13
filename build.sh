#!/usr/bin/env bash

set -xe

#Time=$(date +"%Y%m%d%H%M%S")
# test 文件名必须以 test_ 开头，否则会找不到
TestDir="./testcases"
ReportDir="./.build/allure-report"
ResultDir="./.build/allure-results"
#CurrentResultDir="$ResultDir/$Time"
Environment="./environment.properties"

#mkdir -p "$CurrentResultDir"

#python main.py "$TestDir" "$CurrentResultDir"
python main.py "$TestDir"
#cp $Environment "$CurrentResultDir"
cp $Environment "$ResultDir"

#allure generate --clean -o $ReportDir "$CurrentResultDir"
allure generate --clean -o $ReportDir "$ResultDir"
#allure serve "$CurrentResultDir"
allure serve "$ResultDir"
