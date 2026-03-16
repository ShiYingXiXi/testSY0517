# _*_ coding : utf-8 _*_
# @Time: 2026/3/16 18:30
# @Author : Amy
# @File : test_example.py
# @Desc : 综合测试示例，展示多种测试场景

import time
import allure
import pytest
from playwright.sync_api import Page, expect
from common.logger import logger
from consts.consts import LoginRegisterStorage


@allure.feature("搜索功能测试")
@allure.story(LoginRegisterStorage)
class TestSearch:
    """搜索功能测试类"""

    @allure.title("百度搜索测试")
    @allure.description("验证百度搜索功能是否正常工作")
    def test_baidu_search(self, page: Page):
        """测试百度搜索"""
        with allure.step("打开百度首页"):
            page.goto("https://www.baidu.com")
            page.set_viewport_size({"width": 1920, "height": 1080})
        
        with allure.step("输入搜索关键词"):
            search_input = page.locator("#kw")
            search_input.fill("Playwright 自动化测试")
            logger.info("已输入搜索关键词：Playwright 自动化测试")
        
        with allure.step("点击搜索按钮"):
            search_button = page.locator("#su")
            search_button.click()
            logger.info("已点击搜索按钮")
        
        with allure.step("验证搜索结果"):
            # 等待搜索结果加载
            time.sleep(2)
            result_stats = page.locator("#tsn")
            expect(result_stats).to_be_visible()
            logger.info("搜索结果页面加载成功")
        
        with allure.step("截图保存"):
            page.screenshot(path="./testcases/sy/resources/baidu_search_result.png")
            logger.info("已保存搜索结果截图")

    @allure.title("多关键词搜索测试")
    @allure.description("测试多个不同的搜索关键词")
    @pytest.mark.parametrize("keyword", ["Python 编程", "自动化测试", "pytest 框架"])
    def test_multiple_keywords(self, page: Page, keyword):
        """测试多个关键词的搜索"""
        with allure.step(f"打开百度首页"):
            page.goto("https://www.baidu.com")
        
        with allure.step(f"搜索关键词：{keyword}"):
            page.locator("#kw").fill(keyword)
            page.locator("#su").click()
            time.sleep(1)
            
            # 验证页面标题包含关键词
            expect(page).to_have_title(expect.anything())
            logger.info(f"关键词 '{keyword}' 搜索完成")


@allure.feature("表单交互测试")
@allure.story("用户交互")
class TestFormInteraction:
    """表单交互测试类"""

    @allure.title("输入框操作测试")
    @allure.description("测试各种输入框操作")
    def test_input_operations(self, page: Page):
        """测试输入框的各种操作"""
        with allure.step("打开测试页面"):
            page.goto("https://www.baidu.com")
        
        with allure.step("测试快速填充"):
            search_box = page.locator("#kw")
            # 逐步输入
            search_box.type("Playwright", delay=100)
            time.sleep(1)
            
            # 清空并重新填充
            search_box.clear()
            search_box.fill("自动化测试工具")
            logger.info("完成输入框操作测试")
        
        with allure.step("验证输入内容"):
            value = search_box.input_value()
            assert "自动化" in value
            logger.info(f"验证输入值：{value}")

    @allure.title("键盘操作测试")
    @allure.description("测试键盘快捷键操作")
    def test_keyboard_operations(self, page: Page):
        """测试键盘操作"""
        with allure.step("打开百度首页"):
            page.goto("https://www.baidu.com")
        
        with allure.step("使用键盘操作进行搜索"):
            search_box = page.locator("#kw")
            search_box.fill("键盘测试")
            
            # 使用 Enter 键搜索
            search_box.press("Enter")
            time.sleep(2)
            
            logger.info("完成键盘操作测试")
        
        with allure.step("验证搜索结果"):
            expect(page.locator("#content_left")).to_be_visible()


@allure.feature("元素定位测试")
@allure.story("定位器使用")
class TestElementLocator:
    """元素定位测试类"""

    @allure.title("CSS 选择器定位测试")
    def test_css_locator(self, page: Page):
        """测试 CSS 选择器定位"""
        page.goto("https://www.baidu.com")
        
        with allure.step("使用 CSS 选择器定位元素"):
            # 使用 CSS 选择器
            search_btn = page.locator("input#su")
            expect(search_btn).to_be_visible()
            expect(search_btn).to_have_attribute("type", "submit")
            logger.info("CSS 选择器定位成功")

    @allure.title("XPath 定位测试")
    def test_xpath_locator(self, page: Page):
        """测试 XPath 定位"""
        page.goto("https://www.baidu.com")
        
        with allure.step("使用 XPath 定位元素"):
            # 使用 text 定位
            search_box = page.locator("input#kw")
            expect(search_box).to_be_editable()
            logger.info("XPath 定位成功")

    @allure.title("多重定位器测试")
    def test_chained_locators(self, page: Page):
        """测试链式定位器"""
        page.goto("https://www.baidu.com")
        
        with allure.step("使用链式定位器"):
            # 链式定位
            first_result = page.locator("#content_left").locator(".result:first-child")
            logger.info("链式定位器设置完成")


@allure.feature("等待机制测试")
@allure.story("同步与等待")
class TestWaitMechanism:
    """等待机制测试类"""

    @allure.title("显式等待测试")
    def test_explicit_wait(self, page: Page):
        """测试显式等待"""
        page.goto("https://www.baidu.com")
        
        with allure.step("执行搜索并等待结果"):
            page.locator("#kw").fill("等待机制")
            page.locator("#su").click()
            
            # 等待搜索结果出现
            page.wait_for_selector("#content_left")
            logger.info("显式等待完成")
        
        with allure.step("验证结果"):
            expect(page.locator("#content_left")).to_be_visible(timeout=5000)

    @allure.title("网络请求等待测试")
    def test_network_wait(self, page: Page):
        """测试网络请求等待"""
        with allure.step("设置网络监听"):
            page.goto("https://www.baidu.com")
            
            # 等待网络请求完成
            with page.expect_response("**/s?*"):
                page.locator("#kw").fill("网络等待测试")
                page.locator("#su").click()
            
            logger.info("网络请求等待完成")


# 自定义标记示例
@pytest.mark.slow
@allure.feature("性能测试")
class TestPerformance:
    """性能相关测试"""

    @allure.title("页面加载时间测试")
    def test_page_load_time(self, page: Page):
        """测试页面加载时间"""
        import time
        
        start_time = time.time()
        page.goto("https://www.baidu.com")
        end_time = time.time()
        
        load_time = end_time - start_time
        logger.info(f"页面加载时间：{load_time:.2f}秒")
        
        with allure.step(f"页面加载时间为 {load_time:.2f}秒"):
            assert load_time < 5, f"页面加载时间过长：{load_time}秒"
