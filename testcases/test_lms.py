import asyncio
import time
import allure
from playwright.sync_api import Page, expect


#
# async def first():
#     await asyncio.sleep(2)
#     print("\n==== first =====")
#
#
# async def second():
#     await asyncio.sleep(1)
#     print("\n==== second =====")
#
#
# async def run():
#     start = time.time()
#
#     # await second()
#     # await first()
#
#     f = asyncio.create_task(first())
#     s = asyncio.create_task(second())
#     await f
#     await s
#     # await asyncio.wait([f, s])
#
#     end = time.time()
#     print(f"\n==== third:{end - start}s =====")


# def test_run():
#     print("\n==== a =====")
#     asyncio.run(run())
#     print("\n==== b =====")
# @allure.epic("LMS_Test")
@allure.feature("登录功能")
@allure.story("登录")
@allure.title("登录预期成功")
@allure.description("该用例针对用户登录的场景测试")
# @allure.step("步骤")
# def test_step():
#     pass
#
# # @allure.attach()
# # @allure.severity(allure.severity_level.MINOR)
@allure.issue(
    "http://localhost:63342/test/.build/allure-report/index.html?_ijt=tm54c7up9i1ic238tfmulst7mr&_ij_reload=RELOAD_ON_SAVE#behaviors/fc798277bcb961f4373b3ef634a5b678/e51e03d1848d9111/",
    name="点击，跳转到对应BUG的链接地址")
@allure.testcase(
    "http://localhost:63342/test/.build/allure-report/index.html?_ijt=tm54c7up9i1ic238tfmulst7mr&_ij_reload=RELOAD_ON_SAVE#behaviors/fc798277bcb961f4373b3ef634a5b678/e51e03d1848d9111/",
    name="点击，跳转到对应用例的链接地址")
def test_example(page: Page) -> None:
    page.goto("https://www.tuoyucloud.com/#/login")
    # # @allure.attach()
    page.get_by_placeholder("请输入您的账号").click()
    page.get_by_placeholder("请输入您的账号").fill("sy机构")
    page.get_by_placeholder("请输入您的密码").click()
    page.get_by_placeholder("请输入您的密码").fill("123456")
    page.get_by_role("radio", name="机构管理员").click()
    page.get_by_role("button", name="登录").click()
    page.locator("section").get_by_text("小太阳幼儿托育").click()
    page.get_by_text("查看签到").click()
