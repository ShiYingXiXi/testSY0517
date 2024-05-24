import sys

import pytest

if __name__ == '__main__':
    args = sys.argv[1:]

    # 测试 Case 路径
    testcases = "./testcases"
    if len(args) > 0 and len(args[0]) > 0:
        testcases = args[0]

    # 未设置 resultDir 使用默认的 allure-results，设置则使用设置的
    resultDir = "allure-results"
    if len(args) > 1 and len(args[1]) > 0:
        resultDir = args[1]

    print("====== testDir:" + testcases)
    print("====== resultDir:" + resultDir)
    # 执行测试用例生成测试数据，如果已经存在报告，那就先清空，然后再生成新的测试报告，使用命令： --clean-alluredir
    pytest.main(['-vs', testcases, '--clean-alluredir', '--alluredir', resultDir])
