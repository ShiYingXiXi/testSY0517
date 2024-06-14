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

    # main.py
    import subprocess
    import sys

    # 调用 pytest 并传递 Allure 参数
    cmd = ['pytest', '--verbose', '--alluredir=./.build/allure-results/20240614115328', './testcases']
    subprocess.run(cmd, check=True)
    # 执行测试用例生成测试数据，如果已经存在报告，那就先清空，然后再生成新的测试报告，使用命令： --clean-alluredir
    # pytest.main(['-vs', testcases, '--clean-alluredir', '--alluredir', resultDir])
    # pytest.main(['-vs', testcases, '--alluredir', resultDir])
