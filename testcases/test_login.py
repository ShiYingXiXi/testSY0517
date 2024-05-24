import os

import allure
import pytest
from consts.consts import LoginRegisterStorage
from playwright.sync_api import Page
from common.logger import logger


@allure.step("步骤一：")
def step_1():
    logger.info("步骤一：哈哈哈")


@allure.story(LoginRegisterStorage)
@allure.title("用户登录-预期成功")
@allure.description("该用例是针对 登录-查看 场景的测试")
@allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
@allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
def test_example0(page: Page) -> None:
    print("")


# username = os.getenv("LOGNAME")
# story 设置的是用例模块标题
@allure.story(LoginRegisterStorage)
# title 设置的小标题，功能标题
@allure.title("用户注册-预期成功啦啦啦")
# 描述功能
@allure.description("该用例是针对 注册-查看 场景的测试")
# 点击链接标题跳转
@allure.issue(
    "http://localhost:63342/test/.build/allure-report/index.html?_ijt=fnbfmf4p6u6f3im4d27c4htqok&_ij_reload=RELOAD_ON_SAVE#behaviors/968fefd8e520e1d220d6503040c7c1c4/8e75f107e8acf5c6/",
    name="点击，跳转到对应BUG的链接地址")
@allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
def test_example1(page: Page) -> None:
    # u = username
    # print(u)

    page.goto("https://www.tuoyucloud.com/#/login")
    page.get_by_placeholder("请输入您的账号").click()
    page.get_by_placeholder("请输入您的账号").fill("SY托育机构")
    page.get_by_placeholder("请输入您的密码").click()
    page.get_by_placeholder("请输入您的密码").fill("123456")
    page.get_by_role("radio", name="机构管理员").click()
    page.get_by_role("button", name="登录").click()
